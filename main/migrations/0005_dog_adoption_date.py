# Generated by Django 2.2.4 on 2019-08-15 12:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_document_filename_str'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='adoption_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
