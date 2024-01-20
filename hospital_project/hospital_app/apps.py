# hospital_app/apps.py
from django.apps import AppConfig

class HospitalAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hospital_app'

    def ready(self):
        # Import the models here to avoid circular imports
        try:
            import hospital_app.signals  # Import any signals or models-related code here
        except ImportError:
            pass
