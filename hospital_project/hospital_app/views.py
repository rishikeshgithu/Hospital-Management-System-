# hospital_app/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PatientForm
from .models import Patient
from django.contrib.auth import login
from .forms import PatientForm

def home(request):
    return render(request, 'index.html')

def loginhome(request):
    return render(request, 'loginhome.html')

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})

def validate_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()  # Save data to the database
            return HttpResponse("Form submitted successfully. Data saved to the database.")
    else:
        form = PatientForm()

    return render(request, 'validate_patient.html', {'form': form})

def registration(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PatientForm()

    return render(request, 'registration.html', {'form': form})

def login(request):
    # Add login logic here
    return render(request, 'login.html')

def contact(request):
    return render(request, 'contact.html')
