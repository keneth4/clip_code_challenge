# Generated by Django 3.1.1 on 2021-12-08 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('email', models.CharField(max_length=254, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=254)),
                ('domicilio', models.CharField(default=list, max_length=512)),
                ('telefono', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Platillo',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=254)),
                ('descripcion', models.CharField(max_length=512)),
                ('precio', models.FloatField()),
                ('tipo', models.CharField(choices=[('M', 'Mexicana'), ('I', 'Italiana'), ('J', 'Japonesa')], max_length=1)),
                ('estatus', models.CharField(choices=[('D', 'Disponible'), ('N', 'No disponible')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('total', models.FloatField()),
                ('detalle', models.CharField(default=dict, max_length=4096)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_dinner_api.cliente')),
            ],
        ),
    ]
