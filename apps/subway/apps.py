from django.apps import AppConfig


class SubwayConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.subway'
    verbose_name = '地铁数据管理'
