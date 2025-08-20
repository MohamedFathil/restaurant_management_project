from django.db import models

class Feedback(models.Model):
    comment = models.TextField()
    submitted_at = models.DateTimeField(auto_add_now = True)

    def __str__(self):
        return f"Feedback #{self.id} - {self.comment[:20]}"

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_add_now=True)

    def __str__(self):
        return self.name

class RestaurantAddress(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    opening_hours = models.JSONField(default=dict)

    def __str__(self):
        return self.name