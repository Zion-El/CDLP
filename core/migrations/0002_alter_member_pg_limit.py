# Generated by Django 4.2.1 on 2023-05-17 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='pg_limit',
            field=models.DecimalField(db_comment='This is the payment gateway payment amount limit per user', decimal_places=2, default=0, max_digits=11),
        ),
    ]
