from django.apps import AppConfig


class MockgenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mockgen'
