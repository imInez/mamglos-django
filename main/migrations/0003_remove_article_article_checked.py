# Generated by Django 2.2.4 on 2019-08-05 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_article_article_checked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_checked',
        ),
    ]
