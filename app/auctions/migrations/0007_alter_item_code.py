# Generated by Django 5.2 on 2025-05-01 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_rename_user_bid_bidder_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='code',
            field=models.CharField(default='C52C3CFD76', editable=False, max_length=10, unique=True),
        ),
    ]
