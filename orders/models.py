from django.db import models
from django.contrib.auth.models import User
from products.models import  MenuItem

class OrderStatus(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

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
    created_at = models.DateTimeField(auto_add_now=True)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.username}"
        

