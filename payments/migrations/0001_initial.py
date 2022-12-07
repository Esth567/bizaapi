# Generated by Django 4.1.3 on 2022-12-01 13:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=1, max_length=50, verbose_name='name')),
                ('password', models.CharField(default=1, max_length=50, verbose_name='password')),
                ('phone_number', models.CharField(default=1, max_length=30)),
                ('account_balance', models.CharField(default=0.0, max_length=15)),
                ('account_number', models.CharField(max_length=30, null=True)),
                ('registered_date', models.BooleanField(default=False)),
                ('amount', models.FloatField(default=0.0, max_length=15)),
                ('updated_date', models.DateTimeField(blank=True, default=True)),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]