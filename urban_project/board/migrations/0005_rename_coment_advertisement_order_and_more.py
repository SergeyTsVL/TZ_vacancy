# Generated by Django 5.0.3 on 2024-12-14 14:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_remove_advertisement_author_remove_comment_author'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisement',
            old_name='coment',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='coment',
            new_name='order',
        ),
        migrations.AddField(
            model_name='advertisement',
            name='status',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_name', to=settings.AUTH_USER_MODEL),
        ),
    ]
