# Generated by Django 4.0 on 2024-07-06 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_amount_module4_balance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='module4',
            name='again_customer_order_number',
            field=models.CharField(default='', max_length=1122),
            preserve_default=False,
        ),
    ]