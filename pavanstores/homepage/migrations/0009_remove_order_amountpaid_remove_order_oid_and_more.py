# Generated by Django 4.2.4 on 2023-10-12 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_alter_order_oid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='amountpaid',
        ),
        migrations.RemoveField(
            model_name='order',
            name='oid',
        ),
        migrations.RemoveField(
            model_name='order',
            name='paymentstatus',
        ),
    ]
