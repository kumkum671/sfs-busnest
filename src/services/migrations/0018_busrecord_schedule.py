# Generated by Django 4.2 on 2025-01-26 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0017_remove_busrecord_total_filled_seats_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='busrecord',
            name='schedule',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.schedule'),
        ),
    ]
