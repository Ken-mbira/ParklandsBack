# Generated by Django 3.2.9 on 2021-11-03 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('parking', '0003_parking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('car_plate', models.CharField(max_length=3)),
                ('car_plate_number', models.CharField(max_length=5)),
                ('car_brand', models.CharField(max_length=100)),
                ('completed', models.BooleanField(default=False)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='driving', to=settings.AUTH_USER_MODEL)),
                ('parking', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reservations', to='parking.parking')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reservations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
