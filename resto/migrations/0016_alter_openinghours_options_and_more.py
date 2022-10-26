# Generated by Django 4.1 on 2022-10-26 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0015_alter_openinghours_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='openinghours',
            options={'ordering': ('hours_weekday', 'hours_from_hour')},
        ),
        migrations.AlterField(
            model_name='openinghours',
            name='hours_weekday',
            field=models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')]),
        ),
    ]
