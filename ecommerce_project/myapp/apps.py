from django.apps import AppConfig


class MyappConfig(AppConfig):
    name = 'ecommerce_project.myapp'

    def ready(self):
        import ecommerce_project.myapp.signals


