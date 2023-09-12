from django import forms
from all_app.models import administrator
from all_app.models import Doctor

class UserReg(forms.ModelForm):
    class Meta:
        model = administrator
        fields ="__all__"

class Doctorlist(forms.ModelForm):
    class Meta:
        model = Doctor
        fields ="__all__"