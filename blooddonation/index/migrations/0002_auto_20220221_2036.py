# Generated by Django 3.2.7 on 2022-02-21 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodbank',
            name='type_of_donor',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='type_of_donor',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
