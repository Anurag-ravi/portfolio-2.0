# Generated by Django 3.2.4 on 2021-08-27 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_subskill_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='lastname',
            field=models.CharField(default='', max_length=300),
        ),
    ]
