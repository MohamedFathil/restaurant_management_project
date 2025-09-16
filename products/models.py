from django.db import models


class MenuCategory(models.Model):
    name = models.CharField(max_length=150, unique = True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to="menu_images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    category = models.ForeignKey(
        MenuCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='items'
    )

    def __str__(self):
        return str(self.name)