# Generated by Django 4.2 on 2025-02-07 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0013_remove_route_stops_stop_route'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='busrecord',
            unique_together={('bus', 'registration')},
        ),
        migrations.AddField(
            model_name='busrecord',
            name='min_required_capacity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='busrecord',
            name='drop_booking_count',
        ),
        migrations.RemoveField(
            model_name='busrecord',
            name='pickup_booking_count',
        ),
        migrations.RemoveField(
            model_name='busrecord',
            name='route',
        ),
        migrations.RemoveField(
            model_name='busrecord',
            name='schedule',
        ),
        migrations.RemoveField(
            model_name='busrecord',
            name='total_available_seats',
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_count', models.PositiveIntegerField(default=0)),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='services.busrecord')),
                ('registration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='services.registration')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='services.route')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='services.schedule')),
            ],
            options={
                'unique_together': {('registration', 'record', 'schedule')},
            },
        ),
    ]
