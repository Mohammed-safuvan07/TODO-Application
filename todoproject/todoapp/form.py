from . models import todo
from django import forms

class Form(forms.ModelForm):
    class Meta:
        model = todo
        fields = ['task','priority','date']