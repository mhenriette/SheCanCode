from django import forms
from .models import Signup


class FormSignup(forms.ModelForm):
    class Meta:
        model = Signup
        fields = '__all__'

# class FormLogin(forms.ModelForm):
#     class Meta:
#         model = Login
#         fields = '__all__'
