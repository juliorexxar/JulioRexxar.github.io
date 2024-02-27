# Generated by Django 4.2.4 on 2023-11-17 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaInicio', models.DateField()),
                ('fechaTermino', models.DateField()),
                ('rut', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('numeroHabitacion', models.IntegerField()),
                ('cantidadClientes', models.IntegerField()),
            ],
        ),
    ]
