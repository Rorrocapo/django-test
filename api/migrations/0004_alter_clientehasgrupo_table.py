# Generated by Django 3.2.4 on 2021-07-09 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_clientehasgrupo_rol_grupo'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='clientehasgrupo',
            table='m_clientes_has_m_grupos',
        ),
    ]
