# Generated by Django 4.2 on 2024-05-05 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketApp', '0017_ticket_status_checkout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('Payed', 'Payed'), ('Open', 'Open'), ('Canceled', 'Canceled')], default='Open', max_length=100),
        ),
    ]
