from django import forms
from customers.models import Customer


class CustomerRegisterForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    identity_code = forms.CharField(min_length=10, max_length=10, widget=forms.NumberInput)
    age = forms.IntegerField(widget=forms.NumberInput)
    gender_choices = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    )
    gender = forms.ChoiceField(choices=gender_choices)
    phone_number = forms.CharField(min_length=10, max_length=13)

    def clean(self):
        cleaned_data = self.data
        password = cleaned_data["password"]
        confirm_password = cleaned_data["confirm_password"]
        if password != confirm_password:
            raise forms.ValidationError("Password and confirm password are not the same")
