# Generated by Django 3.1.1 on 2021-12-09 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_dinner_api', '0002_auto_20211209_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='platillo',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
