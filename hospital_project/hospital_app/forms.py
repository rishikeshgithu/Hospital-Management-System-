# hospital_app/forms.py
from django import forms
from .models import Patient

class PatientForm(forms.Form):
    id = forms.CharField(max_length=3)
    firstname = forms.CharField()
    lastname = forms.CharField()
    contactNumber = forms.CharField(max_length=11)
    emailAdress = forms.EmailField()
    history = forms.CharField()
    doctor = forms.CharField()

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'  # Use all fields from the model

class RegistrationForm(PatientForm):
        class Meta:
             model = Patient
             fields = '__all__'  # Use all fields from the model
