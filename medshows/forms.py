from django import forms
from . import models

class MedShowForm(forms.ModelForm):
    class Meta:
        model = models.MedicalShows
        fields = "__all__"
