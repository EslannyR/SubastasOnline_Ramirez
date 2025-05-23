# Generated by Django 5.2 on 2025-04-30 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_alter_item_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='user',
            new_name='bidder',
        ),
        migrations.RenameField(
            model_name='bid',
            old_name='bid_date',
            new_name='created_at',
        ),
        migrations.AlterField(
            model_name='item',
            name='code',
            field=models.CharField(default='534429EC3C', editable=False, max_length=10, unique=True),
        ),
    ]
