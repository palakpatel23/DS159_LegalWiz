# Generated by Django 3.0.8 on 2020-07-30 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20200729_2057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lawyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=15)),
                ('workarea', models.CharField(max_length=50)),
                ('aor', models.CharField(max_length=20)),
            ],
        ),
    ]