from .models import ContactFormSubmission
from rest_framework import serializers

class ContactFormSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactFormSubmission
        fields = ['id','name','email','message','submitted_at']

