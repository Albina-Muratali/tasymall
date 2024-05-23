# Generated by Django 3.2.25 on 2024-05-18 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='delivered_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='delivery_address_photo',
            field=models.ImageField(blank=True, null=True, upload_to='job/delivery_photos/'),
        ),
        migrations.AddField(
            model_name='job',
            name='pickedup_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='pickup_photo',
            field=models.ImageField(blank=True, null=True, upload_to='job/pickup_photos/'),
        ),
    ]