from django.apps import AppConfig


class YogaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'yoga'
    verbose_name = 'Йога'

    def ready(self):
        """
        Ready - это метод, который вызывается при загрузке приложения.
        Мы можем здесь подписываться на сигналы.
        """
        import yoga.signals
