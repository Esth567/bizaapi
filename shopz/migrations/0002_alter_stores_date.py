# Generated by Django 4.1.3 on 2022-12-01 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stores',
            name='date',
            field=models.DateField(),
        ),
    ]