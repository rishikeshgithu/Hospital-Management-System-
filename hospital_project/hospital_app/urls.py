# hospital_app/urls.py
from django.urls import path
from .views import home, validate_patient, registration, login, patient_list,contact,appointments,doctors,services,about_us

urlpatterns = [
    path('', home, name='home'),
    path('validate_patient/', validate_patient, name='validate_patient'),
    path('registration/', registration, name='registration'),
    path('register/', registration, name='registration'),
    path('login/', login, name='login'),
    path('patients/', patient_list, name='patient_list'),
    path('loginhome/', home, name='loginhome'),
    path('contact/', contact, name='contact'),
    path('appointments/', appointments, name='appointments'),
    path('doctors/', doctors, name='doctors'),
    path('services/', services, name='services'),
    path('about_us/', about_us, name='about_us'),
]
