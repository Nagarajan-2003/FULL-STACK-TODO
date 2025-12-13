from django import forms
from .models import *
from .views import *
class TodoForm(forms.ModelForm):
    class Meta:
        model=TodoModel
        fields="__all__"