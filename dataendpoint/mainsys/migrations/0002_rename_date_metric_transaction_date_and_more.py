# Generated by Django 4.1.5 on 2023-01-06 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsys', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='metric',
            old_name='date',
            new_name='transaction_date',
        ),
        migrations.AlterField(
            model_name='metric',
            name='impressions',
            field=models.IntegerField(),
        ),
    ]