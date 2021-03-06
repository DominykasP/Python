# Generated by Django 3.0.6 on 2020-05-20 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('istaiga', models.CharField(max_length=200)),
                ('numeris', models.IntegerField()),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('vieta', models.CharField(max_length=200)),
                ('atsakingas_darbuotojas', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='atsakingas_darbuotojas', to=settings.AUTH_USER_MODEL)),
                ('komisijos_narys', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='komisijos_narys', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PvmForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pavadinimas', models.CharField(max_length=200)),
                ('vnt', models.CharField(max_length=200)),
                ('kiekis', models.IntegerField()),
                ('kaina', models.FloatField()),
                ('suma', models.FloatField()),
                ('vieta', models.CharField(max_length=500)),
                ('forma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pvm_forms.Form')),
            ],
        ),
    ]
