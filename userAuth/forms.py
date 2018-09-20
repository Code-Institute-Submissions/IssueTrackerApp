"""Forms"""
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    """Form for user login"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(UserCreationForm):
    """Form for registering new users"""
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm your password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        """Form validation"""
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        # Check DB if email already used
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError("Account with this email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        # Check if either of those are None
        if not password1 or not password2:
            raise ValidationError("Please confirm your password")
        # Check if passwords don't match
        if password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2
