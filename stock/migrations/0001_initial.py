# Generated by Django 3.0.6 on 2020-05-18 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='Name')),
                ('full_name', models.CharField(max_length=32, verbose_name='Full Name')),
                ('stock_type', models.CharField(choices=[('o', 'otc'), ('e', 'exchange')], max_length=2, verbose_name='Stock Type')),
                ('price', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Stock',
                'verbose_name_plural': 'Stocks',
            },
        ),
        migrations.CreateModel(
            name='UserStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='Amount')),
                ('profit', models.IntegerField(default=0, verbose_name='Profit')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Stock', verbose_name='Stock')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Account', verbose_name='User')),
            ],
            options={
                'verbose_name': 'User-Stock',
                'verbose_name_plural': 'User-stocks',
            },
        ),
    ]
