from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Order, OrderItem, Coupon
from decimal import Decimal
from datetime import timedelta
from django.utils import timezone
from products.models import MenuItem

class OrderModelTest(TestCase):
    def setup(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',email='test@gmail.com', password='password123'
        )
        self.item1 = MenuItem.objects.create(name='Burger', price=Decimal("50.00"))
        self.item2 = MenuItem.objects.create(name='Pizza', price=Decimal("100.00"))
        self.order = Order.objects.create(customer=self.user)

        OrderItem.objects.create(order=self.order, menu_item=self.item1, quantity=2, price=self.item1.price)
        OrderItem.objects.create(order=self.order, menu_item=self.item2, quantity=1, price=self.item2.price)

    def test_calculate_total_without_coupon(self):
        total = self.order.calculate_total()
        self.assertEqual(total, Decimal("200.00"))
    
    def test_calculate_total_with_coupon(self):
        coupon = Coupon.objects.create(
            code="TEST10",
            discount = Decimal("10.00"),
            valid_from = timezone.now() - timedelta(days=1),
            valid_to = timezone.now() + timedelta(days=5),
            active=True
        )
        self.order.coupon = coupon
        self.order.save()

        total = self.order.calculate_total()
        self.assertEqual(total, Decimal("225.00"))
    