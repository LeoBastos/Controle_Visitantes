from django.db import models


class Visitante(models.Model):

    STATUS_VISITANTE = [
        ('AGUARDANDO' , 'Aguardando Autorização'),
        ('EM_VISITA' , 'Em visita'),
        ('FINALIZADO' , 'Visita Finalizada'),
    ]

    status = models.CharField(verbose_name='Status', max_length=10, choices=STATUS_VISITANTE, default="AGUARDANDO")

    nome = models.CharField(max_length=100, verbose_name='Nome Completo')
    cpf = models.CharField(max_length=11, verbose_name='CPF')
    data_Nascimento = models.DateField(auto_now_add=False, auto_now=False, verbose_name='Data de Nascimento')
    numero = models.PositiveSmallIntegerField(verbose_name='Número da Residência')
    placa_veiculo = models.CharField(max_length=7, verbose_name='Placa do Veículo', blank=True, null=True)
    horario_chegada = models.DateTimeField(verbose_name='Horário de chegada na Portaria', auto_now_add=True,)
    horario_saida = models.DateTimeField(verbose_name='Horário de Saída', auto_now=False, blank=True, null=True)
    horario_autorizacao = models.DateTimeField(verbose_name='Horário de Autorização de Entrada', auto_now=False, blank=True, null=True)
    morador_responsavel = models.CharField(verbose_name='Nome do morador responsável por autorizar a entrada do visitante', max_length=100, blank=True)
    registrado_por = models.ForeignKey('porteiros.Porteiro', verbose_name='Porteiro Responsável pelo Registro', on_delete=models.PROTECT)

    def get_horario_saida(self):
        if self.horario_saida:
            return self.horario_saida
        return 'Horario de saida não Registrado.'

    def get_horario_autorizacao(self):
        if self.horario_autorizacao:
            return self.horario_autorizacao
        return 'Visitante aguardando autorização.'
    
    def get_morador_responsavel(self):
        if self.morador_responsavel:
            return self.morador_responsavel
        return 'Visitante aguardando autorização.'

    def get_placa_veiculo(self):
        if self.placa_veiculo:
            return self.placa_veiculo
        return 'Veículo não cadastrado.'

    def get_cpf(self):
        if self.cpf:
            cpf = str(self.cpf)

            cpf1 = cpf[0:3]
            cpf2 = cpf[3:6]
            cpf3 = cpf[6:9]
            cpf4 = cpf[9:]

            cpf_formatado = f'{cpf1}.{cpf2}.{cpf3}-{cpf4}'
            return cpf_formatado
        

    class Meta:
        verbose_name = 'Visitante'
        verbose_name_plural = 'Visitantes'
        db_table = 'visitante'

    def __str__(self):
        return self.nome
