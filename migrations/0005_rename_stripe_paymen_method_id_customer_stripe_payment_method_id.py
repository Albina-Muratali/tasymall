# Generated by Django 3.2.25 on 2024-05-07 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20240507_1617'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='stripe_paymen_method_id',
            new_name='stripe_payment_method_id',
        ),
    ]
