# Generated by Django 4.2.2 on 2023-08-10 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_userdetailsmodel_phone_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bankdetails',
            options={'verbose_name_plural': 'Bank Details'},
        ),
    ]
