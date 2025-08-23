from django import forms
from .models import Contact, Feedback
from django.core.validators import validate_email

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','message']
    
    def clean_email(self):
        email = self.cleaned_data('email')
        validate_email(email)
        return email
    
    def clean_message(self):
        message = self.cleaned_data('message')
        if len(message) < 10:
            raise forms.ValidationError("Message must be at least 10 character long. ")
        return message

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name','feedback']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'your name'}),
            'feedback':forms.Textarea(attrs={'class':'form-control', 'placeholder':'your feedback'}),
        }
