from django.db import models
from django.utils.translation import ugettext_lazy as _

from accounts.models import Account

# Create your models here.


class Stock(models.Model):
    STOCK_TYPE_OTC = 'o'
    STOCK_TYPE_EXCHANGE = 'e'
    STOCK_TYPE_CHOICES = (
        (STOCK_TYPE_OTC, _('otc')),
        (STOCK_TYPE_EXCHANGE, _('exchange')),
    )

    name = models.CharField(max_length=16, verbose_name=_("Name"))
    full_name = models.CharField(max_length=32, verbose_name=_('Full Name'))
    stock_type = models.CharField(max_length=2, verbose_name=_('Stock Type'), choices=STOCK_TYPE_CHOICES)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def __init__(self, *args, **kwargs):
        super(self, Stock).__init__(*args, **kwargs)

    class Meta:
        verbose_name = _('Stock')
        verbose_name_plural = _('Stocks')


class UserStock(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, verbose_name=_('Stock'))
    user = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name=_('User'))
    amount = models.IntegerField(verbose_name=_('Amount'))
    profit = models.IntegerField(default=0, verbose_name=_('Profit'))
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.stock.name, self.user.username)

    def __init__(self, *args, **kwargs):
        super(self, UserStock).__init__(*args, **kwargs)

    class Meta:
        verbose_name = _('User-Stock')
        verbose_name_plural = _('User-stocks')
