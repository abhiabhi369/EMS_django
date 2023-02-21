from django import forms
from django.forms import ModelForm

from Ems_app.models import Users, Country, Voters

class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = '__all__'

class VotersForm(ModelForm):
    class Meta:
        model = Voters
        fields = '__all__'