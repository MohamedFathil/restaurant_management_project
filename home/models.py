from django.db import models

# Create your models here.
class Feedback(models.Model):
    comment = models.TextField()
    submitted_at = models.DateTimeField(auto_add_now = True)

    def __str__(self):
        return f"Feedback #{self.id} - {self.comment[:20]}"