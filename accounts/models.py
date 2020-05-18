from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Account(models.Model):
    first_name = models.CharField(max_length=32, verbose_name=_('first-name'), help_text=_('First-name'))
    last_name = models.CharField(max_length=32, verbose_name=_('last-name'), help_text=_('Last-name'))
    username = models.CharField(max_length=32, verbose_name=_('username'), help_text=_('Username'))
    phone = models.CharField(max_length=16, verbose_name=_('Phone'), help_text=_('Phone'))

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __init__(self, *args, **kwargs):
        super(self, Account).__init__(*args, **kwargs)

    class Meta:
        verbose_name = _('Account')
        verbose_name_plural = _('Accounts')
