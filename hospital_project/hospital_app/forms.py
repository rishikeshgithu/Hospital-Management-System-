# hospital_app/forms.py
from django import forms

class PatientForm(forms.Form):
    id = forms.CharField(max_length=3)
    firstname = forms.CharField()
    lastname = forms.CharField()
    contactNumber = forms.CharField(max_length=11)
    emailAdress = forms.EmailField()
    history = forms.CharField()
    doctor = forms.CharField()
