from django import forms
from .models import ProcessFile

class ProcessFileForm(forms.ModelForm):
    class Meta:
        model = ProcessFile
        fields = ('process', 'file')
        widgets = {
            'process': forms.Select(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
        }
