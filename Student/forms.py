from django import forms
from .models import SelectionStatus

class SelectionStatusForm(forms.ModelForm):
    class Meta:
        model = SelectionStatus
        fields = ['job', 'status']
        widgets = {
            'status': forms.RadioSelect,
        }