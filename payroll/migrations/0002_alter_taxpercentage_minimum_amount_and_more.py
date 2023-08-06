# Generated by Django 4.2.2 on 2023-08-05 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxpercentage',
            name='minimum_amount',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='taxpercentage',
            name='tax_percent',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]