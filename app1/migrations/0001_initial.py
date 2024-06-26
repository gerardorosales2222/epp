# Generated by Django 5.0.6 on 2024-06-21 21:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='material_de_epp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_material', models.CharField(max_length=50, verbose_name='Nombre Material')),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materiales',
                'db_table': 'material',
            },
        ),
        migrations.CreateModel(
            name='tipo_cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cargo', models.CharField(max_length=20, verbose_name='Nombre_Cargo')),
                ('descripción', models.CharField(max_length=100, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'tipo_cargo',
                'verbose_name_plural': 'Tipos de Cargos',
                'db_table': 'tipo_cargo',
            },
        ),
        migrations.CreateModel(
            name='tipo_supervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30, verbose_name='Título')),
                ('descripción', models.CharField(max_length=30, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Tipo de Supervisor',
                'verbose_name_plural': 'Tipos de Supervisores',
                'db_table': 'tipo_supervisor',
            },
        ),
        migrations.CreateModel(
            name='epp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_epp', models.CharField(blank=True, default=0, max_length=40, verbose_name='Nombre del EPP')),
                ('marca', models.CharField(blank=True, max_length=40, null=True, verbose_name='Marca')),
                ('stock', models.IntegerField(default=0, verbose_name='Stock')),
                ('material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.material_de_epp', verbose_name='Material')),
            ],
            options={
                'verbose_name': 'Elemento de Protección Personal',
                'verbose_name_plural': 'Elementos de Protección Personal',
                'db_table': 'epp',
            },
        ),
        migrations.CreateModel(
            name='obreros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legajo', models.CharField(max_length=4, verbose_name='Legajo')),
                ('dni', models.CharField(max_length=8, verbose_name='DNI')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=20, verbose_name='Apellido')),
                ('tel', models.CharField(max_length=10, verbose_name='Teléfono')),
                ('género', models.CharField(choices=[('V', 'Varón'), ('M', 'Mujer')], max_length=1)),
                ('cargo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.tipo_cargo')),
            ],
            options={
                'verbose_name': 'obrero',
                'verbose_name_plural': 'Obreros',
                'db_table': 'obrero',
            },
        ),
        migrations.CreateModel(
            name='supervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legajo', models.CharField(max_length=4, verbose_name='Legajo')),
                ('dni', models.CharField(max_length=8, verbose_name='DNI')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=20, verbose_name='Apellido')),
                ('tel', models.CharField(max_length=10, verbose_name='Teléfono')),
                ('género', models.CharField(choices=[('V', 'Varón'), ('M', 'Mujer')], max_length=1)),
                ('cargo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.tipo_supervisor')),
            ],
            options={
                'verbose_name': 'supervisor',
                'verbose_name_plural': 'Supervisores',
                'db_table': 'supervisor',
            },
        ),
    ]
