# Generated by Django 4.2.2 on 2023-08-05 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_userdetailsmodel_user_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetailsmodel',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
