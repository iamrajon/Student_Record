from django import forms
from core.models import Student


# Student Creation form
class StudentCreationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'email', 'roll', 'address')

    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'Enter Name*',
    }))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'class':'form-control', 'placeholder':'Enter Email Id*',
    }))
    roll = forms.IntegerField(label='Roll', widget=forms.NumberInput(attrs={
        'class':'form-control', 'placeholder':'Enter Roll*',
    }))
    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'Enter Address*',
    }))