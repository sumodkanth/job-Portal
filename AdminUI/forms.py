from django import forms
from .models import Marquee

class MarqueeForm(forms.ModelForm):
    class Meta:
        model = Marquee
        fields = ['text', 'date', 'time']