from django.apps import AppConfig


class NotifyConfig(AppConfig):
    name = 'notify'

    def ready(self):
        try:
            import notify.signals
        except ImportError:
            pass
