# Generated by Django 3.0.6 on 2020-07-31 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_hearing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hearing',
            name='lastHearing',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='hearing',
            name='nextHearing',
            field=models.CharField(max_length=20),
        ),
    ]