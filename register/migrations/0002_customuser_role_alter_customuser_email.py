# Generated by Django 5.1.4 on 2024-12-11 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('student', 'Student'), ('tutor', 'Tutor'), ('admin', 'Admin')], default='student', max_length=10),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
