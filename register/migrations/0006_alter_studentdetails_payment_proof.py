# Generated by Django 5.1.4 on 2024-12-11 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_remove_studentdetails_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='payment_proof',
            field=models.CharField(max_length=5000),
        ),
    ]
