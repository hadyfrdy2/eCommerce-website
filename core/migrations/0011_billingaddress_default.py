# Generated by Django 4.2.4 on 2023-08-09 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_delete_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingaddress',
            name='default',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
