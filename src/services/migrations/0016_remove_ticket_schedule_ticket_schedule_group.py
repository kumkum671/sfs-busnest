# Generated by Django 4.2 on 2025-02-07 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0015_schedulegroup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='schedule',
        ),
        migrations.AddField(
            model_name='ticket',
            name='schedule_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tickets', to='services.schedulegroup'),
        ),
    ]
