# Generated by Django 5.1.1 on 2024-10-09 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_pro_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='decs',
            new_name='decsr',
        ),
    ]
