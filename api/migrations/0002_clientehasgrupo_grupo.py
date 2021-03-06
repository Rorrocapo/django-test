# Generated by Django 3.2.4 on 2021-07-09 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folio_solicitud', models.CharField(max_length=100)),
                ('nombre_grupo', models.CharField(max_length=100)),
                ('usuario_captura', models.CharField(max_length=100)),
                ('usuario_coloca', models.CharField(max_length=100)),
                ('usuario_verifica', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateField()),
                ('monto_total', models.DecimalField(decimal_places=2, max_digits=20)),
                ('plazo_pago', models.IntegerField()),
                ('plazos_forzosos', models.IntegerField()),
                ('garantia_liquida', models.IntegerField()),
                ('num_integrantes', models.IntegerField()),
            ],
            options={
                'db_table': 'tbl_grupos',
            },
        ),
        migrations.CreateModel(
            name='ClienteHasGrupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol_grupo', models.CharField(max_length=100)),
                ('monto_aprobado', models.DecimalField(decimal_places=2, max_digits=20)),
                ('monto_total_pagar', models.DecimalField(decimal_places=2, max_digits=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to='api.cliente')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grupo', to='api.grupo')),
            ],
        ),
    ]
