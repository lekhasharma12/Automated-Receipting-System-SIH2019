# Generated by Django 2.0 on 2019-03-02 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finance', '0010_user_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='company_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='items',
            name='company_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='receiptdata',
            name='company_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='uploads',
            name='company_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
