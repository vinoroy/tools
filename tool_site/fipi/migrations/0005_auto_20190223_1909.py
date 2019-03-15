# Generated by Django 2.1.2 on 2019-02-23 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fipi', '0004_auto_20190223_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='debtFeedRef',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='debtFeedType',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='priceFeedType',
            field=models.CharField(choices=[('YAHOO', 'Yahoo feed')], default='1', max_length=40),
        ),
        migrations.AlterField(
            model_name='asset',
            name='saleDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='salePrice',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='thresholds',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
