from django import forms
from .models import fill

class fillform(forms.ModelForm):
    class Meta:
        model=fill
        fields=['username','password']