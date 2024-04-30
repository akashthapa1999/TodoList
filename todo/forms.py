from django import forms
from .models import TodoModel

class TodoForm(forms.ModelForm):
    Title = forms.CharField(required=True)
    class Meta:
        model = TodoModel
        fields = ["Title"] 
        


