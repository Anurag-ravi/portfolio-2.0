# Generated by Django 3.2.4 on 2021-08-27 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sociallink',
            name='icon',
            field=models.CharField(default='', max_length=300),
        ),
    ]
