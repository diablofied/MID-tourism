# Generated by Django 4.1 on 2022-11-02 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=50)),
                ('hotel_address', models.CharField(max_length=100)),
                ('hotel_photo', models.ImageField(blank=True, null=True, upload_to='hotel/')),
                ('email', models.EmailField(max_length=254)),
                ('star', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type', models.CharField(max_length=50)),
                ('room_description', models.TextField()),
                ('room_photo', models.ImageField(blank=True, null=True, upload_to='room/')),
                ('room_price', models.BigIntegerField()),
                ('is_booked', models.BooleanField(default=False)),
                ('room_hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel')),
            ],
        ),
    ]
