# Generated by Django 3.2.4 on 2021-06-30 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('porteiros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome Completo')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('data_Nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('numero', models.PositiveSmallIntegerField(verbose_name='Número da Residência')),
                ('placa_veiculo', models.CharField(blank=True, max_length=7, null=True, verbose_name='Placa do Veículo')),
                ('horario_chegada', models.DateTimeField(auto_now_add=True, verbose_name='Horário de chegada na Portaria')),
                ('horario_saida', models.DateTimeField(blank=True, null=True, verbose_name='Horário de Saída')),
                ('horario_autorizacao', models.DateTimeField(blank=True, null=True, verbose_name='Horário de Autorização de Entrada')),
                ('morador_responsavel', models.CharField(blank=True, max_length=100, verbose_name='Nome do morador responsável por autorizar a entrada do visitante')),
                ('registrado_por', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='porteiros.porteiro', verbose_name='Porteiro Responsável pelo Registro')),
            ],
            options={
                'verbose_name': 'Visitante',
                'verbose_name_plural': 'Visitantes',
                'db_table': 'visitante',
            },
        ),
    ]