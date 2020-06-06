from django.db import models

# Create your models here.


class Phone(models.Model):
    US_PRE_NUMBER = "+1"
    IRAN_PRE_NUM = "+98"
    UA_PRE_NUMBER = '+971'
    QATAR_PRE_NUMBER = '+974'
    PRE_NUMBER_STATUS = (
        (US_PRE_NUMBER, _('US')),
        (IRAN_PRE_NUM, _('Iran')),
        (UA_PRE_NUMBER, _('United Arab Emirates')),
        (QATAR_PRE_NUMBER, _('Qatar')),
    )

    pre_number = models.CharField(max_length=10, verbose_name=_('Pre Number'), choices=PRE_NUMBER_STATUS)
    number = models.CharField(max_length=11, verbose_name=_('Phone Number'))

    def __str__(self):
        return self.number

    def __init__(self, *args, **kwargs):
        super(Phone, self).__init__(*args, **kwargs)

    class Meta:
        verbose_name = _('Phone')
        verbose_name_plural = _('Phones')
