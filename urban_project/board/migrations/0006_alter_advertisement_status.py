# Generated by Django 5.0.3 on 2024-12-14 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_rename_coment_advertisement_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='status',
            field=models.CharField(max_length=255),
        ),
    ]
