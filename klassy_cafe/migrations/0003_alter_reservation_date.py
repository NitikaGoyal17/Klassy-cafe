# Generated by Django 4.2.7 on 2023-12-13 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klassy_cafe', '0002_alter_reservation_date_alter_reservation_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(null=True),
        ),
    ]