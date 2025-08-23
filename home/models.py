from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    feedback = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Feedback #{self.name} - {self.submitted_at.strftime('%Y-%m-%d)}"

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class RestaurantAddress(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    opening_hours = models.JSONField(default=dict)

    def __str__(self):
        return self.name

class RestaurantLocation(models.Model):
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.address}, {self.city}, {self.state}, {self.zip_code}"

# for setup logo
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, null=True, blank=True)
    logo = models.ImageField(upload_to="restaurant_logos/", blank=True, null=True)

    def __str__(self):
        return self.name
