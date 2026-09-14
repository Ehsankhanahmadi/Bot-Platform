from django import forms
from .models import RunTime



class RunTimeAdminForm(forms.ModelForm):
    class Meta:
        model = RunTime
        fields = "__all__"