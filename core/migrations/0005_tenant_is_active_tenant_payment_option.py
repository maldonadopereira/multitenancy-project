# Generated by Django 5.0.2 on 2024-02-11 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_mydomain_domain'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tenant',
            name='payment_option',
            field=models.CharField(choices=[('monthly', 'Monthly'), ('annual', 'Annual')], default='monthly', max_length=50),
        ),
    ]
