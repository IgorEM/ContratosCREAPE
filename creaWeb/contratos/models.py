from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Create your models here.
class Contratos(models.Model):
    SITUACAO_CHOICES = (
        ('ATIVO', 'ATIVO'),
        ('ENCERRADO', 'ENCERRADO'),
        ('VENCIDO', 'VENCIDO')
    )
    numero_Do_Contrato = models.CharField(max_length=15)
    contratada	= models.CharField(max_length=150)
    objeto = models.CharField(max_length=500)
    fiscal_Do_Contrato = models.CharField(max_length=50)
    vigencia_Inicio = models.DateField(verbose_name='Vigência Inicio')
    vigencia_Fim = models.DateField(verbose_name='Vigência Fim')
    valor_Do_Contrato = models.FloatField()
    limite_A_Licitar = models.DateField(verbose_name='Limite a Licitar')
    situacao_Do_Contrato = models.CharField(max_length=12, choices=SITUACAO_CHOICES)
    numero_Do_Aditivo = models.PositiveIntegerField(max_length=1)
    aditivo_Valores = models.FloatField()
    vigencia_Inicio_Aditivo = models.DateField(verbose_name='Vigência Inicio Aditivo')
    vigencia_Fim_Aditivo  = models.DateField(verbose_name='Vigência Fim Aditivo')
    #num_Dias_Para_o_Vencimento = models.PositiveIntegerField(max_length=1)
    #num_de_Dias_Vencido = models.IntegerField()
    andamento_e_outras_informacoes	= models.CharField(max_length=500)
    fundamento_Legal = models.CharField(max_length=100)

    @property
    def dias_Para_Vencer(self):
        data_atual = date.today()
        diasParaVencer = relativedelta(data_atual, self.vigencia_Fim_Aditivo).days
        return diasParaVencer

    class Meta: #metadados da tabela, forçando o nome da tabela core_evento se tornar evento
        db_table = 'dadosContratos'

    def __str__(self): #agora o evento aparece como object 1
        return f"{self.numero_Do_Contrato} - {self.contratada} - {self.numero_Do_Aditivo}"

    def dataVigIniCon(self):
        return self.vigencia_Inicio.strftime("%d/%m/%Y")

    def dataVigFimCon(self):
        return self.vigencia_Fim.strftime("%d/%m/%Y")

    def dataVigIniAdi(self):
        return self.vigencia_Inicio_Aditivo.strftime("%d/%m/%Y")

    def dataVigFimAdi(self):
        return self.vigencia_Fim_Aditivo.strftime("%d/%m/%Y")


    def get_contratos_atrasado(self):
        if self.num_de_Dias_Vencido < datetime.now() - timedelta(hours=1):
            return True
        else:
            return False