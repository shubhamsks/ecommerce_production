# Generated by Django 2.2.4 on 2019-10-18 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='marketingmessage',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
