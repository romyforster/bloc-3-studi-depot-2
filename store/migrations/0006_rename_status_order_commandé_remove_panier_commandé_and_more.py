# Generated by Django 4.2.5 on 2023-11-13 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_panier'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='status',
            new_name='commandé',
        ),
        migrations.RemoveField(
            model_name='panier',
            name='commandé',
        ),
        migrations.RemoveField(
            model_name='panier',
            name='date_commande',
        ),
        migrations.AddField(
            model_name='order',
            name='date_commande',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
