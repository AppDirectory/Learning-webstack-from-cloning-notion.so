# Generated by Django 3.1 on 2020-08-17 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200812_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elements',
            name='style',
            field=models.JSONField(blank=True, null=True),
        ),
    ]