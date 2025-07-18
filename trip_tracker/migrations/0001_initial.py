# Generated by Django 5.2.3 on 2025-06-19 00:16

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=2)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('type', models.CharField(choices=[('event', 'Event'), ('dining', 'Dining'), ('experience', 'Experience'), ('general', 'General')], max_length=100)),
                ('img', models.ImageField(blank=True, null=True, upload_to='notes')),
                ('rating', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5)])),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='trip_tracker.trip')),
            ],
        ),
    ]
