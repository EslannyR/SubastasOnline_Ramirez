# Generated by Django 5.2 on 2025-04-07 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_item_image1_item_image2_item_image3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
