# Generated by Django 4.1 on 2022-10-28 07:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rental_transport', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transportlist',
            name='availability',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='transportlist',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='transportlist',
            name='transport_name',
            field=models.CharField(max_length=50),
        ),
    ]