# Generated by Django 3.0.6 on 2020-05-21 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pvm_forms', '0005_auto_20200521_0350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='pardavejas',
            field=models.CharField(max_length=200),
        ),
    ]