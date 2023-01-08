from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

        widgets={
            'recorded_on':forms.DateTimeInput(attrs={
             'type':'datetime-local'   
            })
        }

