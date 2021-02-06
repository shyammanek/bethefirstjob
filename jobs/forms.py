from django.forms import ModelForm
from django import forms
from jobs.models import joblist


class todoform(forms.ModelForm):
    class Meta:
        model = joblist
        fields = "__all__"
