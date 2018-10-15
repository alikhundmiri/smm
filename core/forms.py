from django import forms
from django.core.validators import validate_email

from .models import interested

# Form for "interested"
class InterestedForm(forms.ModelForm):
    class Meta:
        model = interested
        fields = [
        'email_address',
        'interested_in',
        ]


    def clean_contact(self):
        this_email = self.cleaned_data.get('email_address')
        this_interest = self.cleaned_data.get('interested_in')
        try:
            validate_email(this_email)
        except forms.ValidationError:
            raise forms.ValidationError("Please enter a Valid Email address")

        existing_email = interested.objects.filter(email_address=this_email, interested_in=this_interest)

        if existing_contact:
            print("CONFLICT OF EMAILS")
            raise forms.ValidationError("You already submitted a request with these credentials")
        else:
            print("NO CONFLICT FOUND")
            return this_email

    def __init__(self, *args , **kwargs):
        super(InterestedForm, self).__init__(*args, **kwargs)
        self.fields["email_address"].help_text = "Please expect our email with in 24 hours."
        self.fields["email_address"].label = "Your Email Addresss"
        self.fields["interested_in"].help_text = "Please expect our email with in 24 hours."
        self.fields["interested_in"].label = "Your Email Addresss"