from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class ToDo(models.Model):
    text = models.CharField(max_length=64, verbose_name=_('Text'))
    done = models.BooleanField(verbose_name=_('Done'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date Created'))

    def __str__(self):
        return self.text

    def __init__(self, *args, **kwargs):
        super(ToDo, self).__init__(*args, **kwargs)

    class Meta:
        verbose_name = _('ToDo')
        verbose_name_plural = _('ToDos')


