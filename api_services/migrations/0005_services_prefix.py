# Generated by Django 4.1.4 on 2022-12-27 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_services', '0004_alter_services_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='prefix',
            field=models.CharField(default='NS', max_length=3),
        ),
    ]
