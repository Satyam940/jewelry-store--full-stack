from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Review_Ring, Review_Necklace , Order
from django.shortcuts import get_object_or_404


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254 , required=True)
    class Meta:
        model = User
        fields=('username', 'email','password1','password2')



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


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name','address' , 'email', 'phone_number', 'city', 'state']

