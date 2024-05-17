from django import forms
from .models import Students


class student_form(forms.ModelForm):
    class Meta:
        model=Students
        fields=['name','father_name',"phone",'email','address']
        widgets ={
             'name':forms.TextInput(attrs={'class':'form-control'}),
             'father_name':forms.TextInput(attrs={'class':'form-control'}),
             'phone':forms.TextInput(attrs={'class':'form-control'}),
             'email':forms.EmailInput(attrs={'class':'form-control'}),
             'address':forms.TextInput(attrs={'class':'form-control'}),

           }
