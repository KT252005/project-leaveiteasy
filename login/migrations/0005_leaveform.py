# Generated by Django 5.1.2 on 2025-04-23 19:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_chat_signup_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('Address', models.CharField(max_length=200)),
                ('City', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=30)),
                ('Zipcode', models.CharField(max_length=6)),
                ('Room_number', models.IntegerField(unique=True)),
                ('enrollment_number', models.CharField(max_length=12)),
                ('submitted_on', models.DateTimeField(auto_now_add=True)),
                ('Parents_contact_number', models.CharField(max_length=10)),
                ('Destination', models.CharField(max_length=60)),
                ('Leave_From_date', models.DateField()),
                ('Leave_to_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.chat_signup')),
            ],
        ),
    ]
