from .models import ContactFormSubmission
from products.models import MenuItem
from rest_framework import serializers

class ContactFormSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactFormSubmission
        fields = ['id','name','email','message','submitted_at']

class DailySpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id','name','description','price']

