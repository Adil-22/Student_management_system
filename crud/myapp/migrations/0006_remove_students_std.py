# Generated by Django 4.2.3 on 2023-09-16 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_students_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='std',
        ),
    ]