from django.db import models


class Porteiro(models.Model):
    usuario = models.OneToOneField('usuarios.Usuario',verbose_name='Usuário', on_delete=models.PROTECT)
    nome = models.CharField(max_length=200, verbose_name='Nome Completo')
    cpf = models.CharField(max_length=11, verbose_name='CPF')
    telefone = models.CharField(max_length=11, verbose_name='Telefone de Contato')
    data_Nascimento = models.DateField(auto_now_add=False, auto_now=False,verbose_name='Data de Nascimento')

    class Meta:
        verbose_name = 'Porteiro'
        verbose_name_plural = 'Porteiros'
        db_table = 'porteiro'

    def __str__(self):
        return self.nome