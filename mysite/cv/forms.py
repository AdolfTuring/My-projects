from django.forms import ModelForm

from .models import Bd

class BdForm(ModelForm):
    class Meta:
        model=Bd
        fields=('fact', 'content', 'level', 'rubric')