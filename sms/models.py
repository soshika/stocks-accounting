from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class SMS(models.Model):
    status = models.BooleanField(verbose_name=_('Status'))
    date_created = models.DateTimeField(auto_now_add=True)
    message = models.TextField(max_length=256, verbose_name=_('Message'))

    def __str__(self):
        return self.message

    def __init__(self, *args, **kwargs):
        super(SMS, self).__init__(*args, **kwargs)

    def send_to_one(self, phone):
        pass

    def send_to_all(self, phones):
        pass

    class Meta:
        verbose_name = _('SMS')
