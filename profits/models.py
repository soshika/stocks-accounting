from django.db import models
from django.utils.translation import ugettext_lazy as _

from stock.models import UserStock
# Create your models here.


class Profit(models.Model):
    PERCENT_TYPE_HOST = 10
    PERCENT_TYPE_BROKER = 40
    PERCENT_TYPE_MAINTAINER = 50
    PERCENT_TYPE_CHOICES = (
        (PERCENT_TYPE_HOST, _('Host')),
        (PERCENT_TYPE_BROKER, _('Broker')),
        (PERCENT_TYPE_MAINTAINER, _('Maintainer')),
    )

    user_stock = models.ForeignKey(UserStock, on_delete=models.CASCADE, related_name='user_stocks')
    host_percent = models.IntegerField(verbose_name=_('Host Percent'))
    broker_percent = models.IntegerField(verbose_name=_('Broker Percent'))
    maintainer_percent = models.IntegerField(verbose_name=_('Maintainer percent'))

    def __str__(self):
        return ''

    def __init__(self, *args, **kwargs):
        super(Profit, self).__init__(*args, **kwargs)

    def calculate_profit(self):
        profit = self.user_stock.profit
        self.host_percent = profit * (self.PERCENT_TYPE_HOST / 100)
        self.broker_percent = profit * (self.PERCENT_TYPE_BROKER / 100)
        self.maintainer_percent = profit * (self.PERCENT_TYPE_MAINTAINER / 100)
        self.save()

    class Meta:
        verbose_name = _('Profit')
        verbose_name_plural = _('Profits')



