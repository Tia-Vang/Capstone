from django.apps import AppConfig


class HomechefappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'homechefapp'

    def ready(self):
       import homechefapp.signals
