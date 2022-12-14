# Generated by Django 4.1 on 2022-11-02 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resto_name', models.CharField(max_length=64)),
                ('resto_address', models.CharField(max_length=128)),
                ('resto_email', models.EmailField(max_length=254)),
                ('resto_phone', models.BigIntegerField()),
                ('resto_description', models.TextField()),
                ('resto_photo', models.ImageField(blank=True, null=True, upload_to='resto/')),
                ('resto_delivery', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=64)),
                ('food_price', models.IntegerField()),
                ('food_stock', models.BooleanField()),
                ('food_description', models.TextField()),
                ('food_photo', models.ImageField(blank=True, null=True, upload_to='food/')),
                ('food_resto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resto.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='OpeningHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours_weekday', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')])),
                ('hours_from_hour', models.TimeField()),
                ('hours_to_hour', models.TimeField()),
                ('hours_restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resto.restaurant')),
            ],
            options={
                'ordering': ('hours_weekday', 'hours_from_hour'),
                'unique_together': {('hours_weekday', 'hours_from_hour', 'hours_to_hour', 'hours_restaurant')},
            },
        ),
    ]
