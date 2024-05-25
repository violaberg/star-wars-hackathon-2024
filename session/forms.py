from .models import Session
from django import forms

class SessionForm(forms.ModelForm):

    class Meta:
        model = Session
        fields = ('character','level')