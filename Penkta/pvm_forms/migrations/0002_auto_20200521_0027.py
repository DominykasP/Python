# Generated by Django 3.0.6 on 2020-05-20 21:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pvm_forms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='komisijos_nariai',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pvmform',
            name='forma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pvmforms', to='pvm_forms.Form'),
        ),
    ]
