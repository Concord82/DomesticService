from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CatalogsConfig(AppConfig):
    name = 'catalogs'
    verbose_name = _('Catalogs')