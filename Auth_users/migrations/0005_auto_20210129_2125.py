# Generated by Django 3.1 on 2021-01-29 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Auth_users', '0004_auto_20210129_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
