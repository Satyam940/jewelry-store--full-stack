from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Review_Ring, Review_Necklace , Order, Review_bangle,OTP
from django.shortcuts import get_object_or_404




class SignUpForm(UserCreationForm):
    

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        print(f"Cleaning username: {username}")  # Debug print
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            print(f"Existing user found: {user.username}, active: {user.is_active}")  # Debug print
            if user.is_active:
                raise forms.ValidationError("A user with that username already exists.")
            else:
                print("Existing user is inactive, allowing update")  # Debug print
        else:
            print("Username is new")  # Debug print
        return username




class Ring_Review(forms.ModelForm):
    class Meta:
        model = Review_Ring
        fields = ['rating','comment']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }


class Necklace_Review(forms.ModelForm):
    class Meta:
        model = Review_Necklace
        fields = ['rating','comment']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }

class Bangle_Review(forms.ModelForm):
    class Meta:
        model = Review_bangle 
        fields = ['rating','comment']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name','address' , 'email', 'phone_number', 'city', 'state']




class otpform(forms.Form):
    otp_code = forms.IntegerField(required=True)