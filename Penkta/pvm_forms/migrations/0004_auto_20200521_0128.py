# Generated by Django 3.0.6 on 2020-05-20 22:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pvm_forms', '0003_remove_form_komisijos_narys'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='atsakingas_darbuotojas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='atsakingas_darbuotojas', to=settings.AUTH_USER_MODEL),
        ),
    ]
