# Generated by Django 5.1 on 2024-08-26 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Temp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=1000)),
                ('summary', models.CharField(max_length=1000000000000000000000000000000)),
            ],
        ),
    ]
