# Generated by Django 5.0.3 on 2024-12-14 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_advertisement_telephone_comment_telephone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
    ]
