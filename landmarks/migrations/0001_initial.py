# Generated by Django 4.1 on 2022-11-02 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Landmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('location', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='landmarks/')),
            ],
        ),
    ]
