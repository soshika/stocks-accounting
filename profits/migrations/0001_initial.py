# Generated by Django 3.0.6 on 2020-05-30 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_percent', models.IntegerField(verbose_name='Host Percent')),
                ('broker_percent', models.IntegerField(verbose_name='Broker Percent')),
                ('maintainer_percent', models.IntegerField(verbose_name='Maintainer percent')),
                ('user_stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_stocks', to='stock.UserStock')),
            ],
            options={
                'verbose_name': 'Profit',
                'verbose_name_plural': 'Profits',
            },
        ),
    ]
