# hospital_app/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .forms import PatientForm

def home(request):
    return render(request, 'index.html')

def validate_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            return HttpResponse("Form is valid. You can process the data here.")
    else:
        form = PatientForm()

    return render(request, 'validate_patient.html', {'form': form})

def registration(request):
    # Add registration logic here
    return render(request, 'registration.html')

def login(request):
    # Add login logic here
    return render(request, 'login.html')
