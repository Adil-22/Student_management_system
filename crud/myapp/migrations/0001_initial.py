# Generated by Django 4.2.3 on 2023-09-15 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('father_name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=500)),
            ],
        ),
    ]
