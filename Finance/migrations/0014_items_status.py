# Generated by Django 2.1 on 2019-03-03 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finance', '0013_merge_20190302_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
