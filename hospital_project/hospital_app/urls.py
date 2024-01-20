# hospital_app/urls.py
from django.urls import path
from .views import home, validate_patient, registration, login, patient_list

urlpatterns = [
    path('', home, name='home'),
    path('validate_patient/', validate_patient, name='validate_patient'),
    path('registration/', registration, name='registration'),
    path('register/', registration, name='registration'),
    path('login/', login, name='login'),
    path('patients/', patient_list, name='patient_list'),
    path('loginhome/', home, name='loginhome'),
]
