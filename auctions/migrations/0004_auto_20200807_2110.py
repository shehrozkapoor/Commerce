# Generated by Django 3.0.8 on 2020-08-07 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_closed_auctions_auction'),
    ]

    operations = [
        migrations.AddField(
            model_name='closed_auctions',
            name='bid',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='closed_auctions',
            name='username',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
