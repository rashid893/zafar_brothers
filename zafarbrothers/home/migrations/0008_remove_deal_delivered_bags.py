# Generated by Django 5.0.7 on 2024-08-21 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_deal_total_dispatch_module3_total_dispatch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deal',
            name='delivered_bags',
        ),
    ]
