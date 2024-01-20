# hospital_app/urls.py
from django.urls import path
from .views import home, validate_patient, registration, login

urlpatterns = [
    path('', home, name='home'),
    path('validate_patient/', validate_patient, name='validate_patient'),
    path('registration/', registration, name='registration'),
    path('login/', login, name='login'),
]
