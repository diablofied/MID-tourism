# Generated by Django 4.1 on 2022-10-29 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental_transport', '0004_alter_transportlist_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transportlist',
            name='availability',
            field=models.CharField(default='Available', max_length=10),
        ),
    ]