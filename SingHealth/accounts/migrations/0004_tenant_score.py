# Generated by Django 3.0.3 on 2021-03-14 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210313_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='score',
            field=models.FloatField(null=True),
        ),
    ]
