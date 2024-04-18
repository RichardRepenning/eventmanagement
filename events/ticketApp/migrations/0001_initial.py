# Generated by Django 4.2 on 2024-04-18 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('street', models.CharField(max_length=200)),
                ('zip_code', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('max_participants', models.IntegerField()),
                ('active', models.BooleanField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketApp.venue')),
            ],
        ),
    ]
