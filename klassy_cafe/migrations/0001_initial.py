# Generated by Django 4.2.7 on 2023-12-11 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(null=True)),
                ('number_guests', models.IntegerField(null=True)),
                ('date', models.IntegerField(null=True)),
                ('time', models.IntegerField(null=True)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
    ]