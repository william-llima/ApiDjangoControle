# Generated by Django 4.1.4 on 2022-12-09 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Motorista',
            fields=[
                ('Cod_Motorista', models.AutoField(primary_key=True, serialize=False)),
                ('Nome', models.CharField(max_length=200)),
                ('Telefone', models.CharField(max_length=20)),
                ('CNH', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('Placa', models.AutoField(primary_key=True, serialize=False)),
                ('Marca', models.CharField(max_length=50)),
                ('Veiculo', models.CharField(max_length=100)),
                ('Km_Troca_Oleo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Controle',
            fields=[
                ('controle_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Data_saida', models.DateField(max_length=12)),
                ('Hora_saida', models.TimeField(max_length=20)),
                ('Km_saida', models.CharField(max_length=20)),
                ('Destino', models.CharField(max_length=300)),
                ('Data_retorno', models.DateField(max_length=12)),
                ('Hora_retorno', models.TimeField(max_length=20)),
                ('Km_Retorno', models.CharField(max_length=20)),
                ('Km_percorrido', models.CharField(max_length=20)),
                ('Motorista', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.motorista')),
                ('Veiculo', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.veiculo')),
            ],
        ),
    ]