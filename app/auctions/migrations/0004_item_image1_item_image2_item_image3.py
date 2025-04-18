# Generated by Django 5.2 on 2025-04-06 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_user_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='item_images/'),
        ),
        migrations.AddField(
            model_name='item',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='item_images/'),
        ),
        migrations.AddField(
            model_name='item',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='item_images/'),
        ),
    ]
