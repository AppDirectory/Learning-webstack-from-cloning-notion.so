# Generated by Django 3.1 on 2020-09-05 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20200905_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elements',
            name='table',
            field=models.JSONField(blank=True, null=True),
        ),
    ]