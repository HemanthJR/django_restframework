# Generated by Django 5.1.4 on 2024-12-11 09:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_customuser_role_alter_customuser_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile', models.CharField(blank=True, max_length=15)),
                ('age', models.IntegerField(max_length=5, null=True)),
                ('city', models.CharField(max_length=225)),
                ('occupation', models.CharField(choices=[('student', 'student'), ('working_professional', 'working professional'), ('freelancer', 'freelancer'), ('others', 'others')], max_length=50)),
                ('institute_name', models.CharField(blank=True, max_length=255, null=True)),
                ('interest', models.CharField(blank=True, max_length=255, null=True)),
                ('worked_in_ai_ml', models.BooleanField()),
                ('ai_experience_details', models.TextField(blank=True, null=True)),
                ('excited_to_learn', models.JSONField(default=list)),
                ('session_timing', models.CharField(blank=True, choices=[('morning', 'Morning (9:00 AM - 12:30 PM)'), ('afternoon', 'Afternoon (1:30 PM - 5:30 PM)'), ('full_day', 'Full Day (9:00 AM - 5:30 PM)')], max_length=50, null=True)),
                ('payment_proof', models.FileField(upload_to='payment_proofs/')),
                ('agreement', models.BooleanField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
