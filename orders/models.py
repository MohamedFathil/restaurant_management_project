from django.db import models
from django.contrib.auth.models import User
from products.models import  MenuItem

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    order_items = models.ManyToMany(MenuItem, related_name="orders")
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    order_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_add_now=True)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.username}"
        
