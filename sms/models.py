from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class SMS(models.Model):
    message = models.TextField()
    phone = models.CharField()

    def __str__(self):
        pass

    def __init__(self, *args, **kwargs):
        super(SMS, self).__init__(*args, **kwargs)

    class Meta:
        verbose_name = _('')
        verbose_name_plural = _('')
