# Generated by Django 4.2.4 on 2023-10-11 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_rename_order_id_order_oid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderupdate',
            old_name='oid',
            new_name='order_id',
        ),
    ]
