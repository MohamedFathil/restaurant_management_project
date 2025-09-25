from django.db import models
from django.contrib.auth.models import User
from products.models import  MenuItem
from decimal import Decimal, ROUND_HALF_UP
from django.conf import settings
from django.utils import timezone
from .utils import calculate_discount

class Coupon(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, help_text='Discount in %')
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code
    
    def is_valid(self):
        return self.active and self.valid_from <= now <= self.valid_to

class OrderStatus(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class OrderManager(models.Manager):

    def by_status(self, status_name):
        return self.filter(status__iexact = status_name)
    
    def pending(self):
        return self.by_status('pending')

    def processing(self):
        return self.by_status('processing')

    def completed(self):
        return self.by_status('completed')
    
    def cancelled(self):
        return self.by_status('cancelled')

class ActiveOrderManager(models.Manager):
    """Custom manager to filter active order"""
    def get_active_orders(self):
        return self.filter(status__name__in = ['pending', 'processing'])

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending','Pending'),
        ('processing','Processing'),
        ('completed','Completed'),
        ('cancelled','Cancelled'),
    ]
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    order_items = models.ManyToManyField(MenuItem, related_name="orders")
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.ForeignKey(
        OrderStatus,
        on_delete = models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    unique_id = models.CharField(max_length=12, unique=True, editable=False)
    objects = OrderManager()

    # calculate the total amount here
    def calculate_total(self):
        total = Decimal("0.00")
        for item in self.items.all():
            total += item.line_total()
        if self.coupon and self.coupon.is_valid():
            total = calculate_discount(total, coupon=self.coupon)
        return total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    def update_total(self):
        self.total_amount = self.calculate_total()
        self.save(update_fields=["total_amount"])
    
    def save(self, *args, **kwargs):
        from .utils import generate_unique_order_id
        if not self.unique_id:
            self.unique_id = generate_unique_order_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.username}"
        
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def line_total(self):
        return (self.price*self.quantity).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    
    def __str__(self):
        return f"{self.menu_item.name} x {self.quantity}"