from django.apps import AppConfig
from django.db.models.signals import post_migrate

class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'

    def ready(self):
        from .models import OrderStatus
        from . import DEFAULT_STATUSES

        def create_statuses(sender, **kwargs):
            for status in DEFAULT_STATUSES:
                OrderStatus.objects.get_or_create(name=status)

        post_migrate.connect(create_statuses, sender=self)

