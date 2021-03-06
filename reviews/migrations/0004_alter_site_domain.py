# Generated by Django 4.0.2 on 2022-02-20 07:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_alter_site_domain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='domain',
            field=models.CharField(max_length=63, unique=True, validators=[django.core.validators.RegexValidator('^[a-z0-9]+\\.[a-z]+$', message='Domain names can only use letters, and numbersDomains cannot exceed 63 characters. ')]),
        ),
    ]
