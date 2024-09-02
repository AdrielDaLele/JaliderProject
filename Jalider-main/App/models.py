from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.core.validators import FileExtensionValidator

GENERO = [
    ("M","MASCULINO"),
    ("F","FEMININO"),
]

class User(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField("endereço do email", unique=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    endereco = models.CharField(max_length=200)
    cfp = models.CharField(max_length=20)
    rg = models.CharField(max_length=13)
    gen = models.CharField(max_length= 200, choices=GENERO)

    def __str__(self):
        return self.nome
    
class Foto(models.Model):
    url = models.CharField(max_length=1000)

    def __srt__(self):
        return self.url
    
class OleoFiltro(models.Model):
    oleo = models.CharField(max_length=120)
    filtro = models.CharField(max_length=120)
    km_oleo = models.IntegerField()

    def __str__(self):
        return self.oleo

class PastilhaDeFreio(models.Model):
    pastilha = models.CharField(max_length=120)
    km_pastilha = models.IntegerField()

    def __str__(self):
        return self.pastilha
    
class CorreiaDentalha(models.Model):
    correia_dentalha = models.CharField(max_length=120)
    km_correia = models.IntegerField()

    def __str__(self):
        return self.correia_dentalha
    
class CaboDeVela(models.Model):
    cabo_de_vela = models.CharField(max_length=120)
    km_cabo_vela = models.IntegerField()

    def __str__(self):
        return self.cabo_de_vela

class Pneu(models.Model):
    pneu = models.CharField(max_length=120)
    km_pneu = models.IntegerField()

    def __str__(self):
        return self.pneu
    
class FiltroArCondicionado(models.Model):
    filtro_ar_condicionado = models.CharField(max_length=120)
    km_filtro_ar_condicionado = models.IntegerField()

    def __str__(self):
        return self.filtro_ar_condicionado

class FiltroGas(models.Model):
    filtro_gas = models.CharField(max_length=120)
    km_filtro = models.IntegerField()

    def __str__(self):
        return self.filtro_gas
    
TIPO_COMBUSTIVEL = [
    ('G','Gas'),
    ('P','Gasolina'),
    ('E','Etanol')
] 

class Carro(models.Model):
    placa = models.CharField(max_length=7)
    modelo = models.CharField(max_length=60)
    ano = models.IntegerField()
    kilometragem = models.IntegerField()
    usuarioFK = models.ForeignKey(User, related_name='UserCarroFK', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50,choices=TIPO_COMBUSTIVEL)
    fotoFK = models.ForeignKey(Foto, related_name='FotoCarroFK', on_delete=models.CASCADE)

    def __str__(self):
        return self.placa


class Manutencao(models.Model):
    manutencao = models.CharField(max_length=100)
    carroFK = models.ForeignKey(Carro, related_name='ManutencaoCarro', on_delete=models.CASCADE)
    # oleoFiltroFK = models.ForeignKey(OleoFiltro, related_name='ManutencaoOleoFiltroFK', on_delete=models.CASCADE) #feito
    # pastilhaDeFreioFK = models.ForeignKey(PastilhaDeFreio, related_name='ManutencaoPastilhaDeFreioFK', on_delete=models.CASCADE)
    # correiaDentalhaFK = models.ForeignKey(CorreiaDentalha, related_name='ManutencaoCorreiaDentalhaFK', on_delete=models.CASCADE)
    # pneuFK = models.ForeignKey(Pneu, related_name='ManutencaoPneuFK', on_delete=models.CASCADE)
    # filtroArCondicionadoFK = models.ForeignKey(FiltroArCondicionado, related_name='ManutencaoFiltroArCondicionadoFK', on_delete=models.CASCADE)
    # filtroGasFK = models.ForeignKey(FiltroGas, related_name='ManutencaoFiltroGasFK', on_delete=models.CASCADE)

    def __str__(self):
        return self.manutencao
    
class ManOleoFiltro(models.Model):
    manutencaoFK = models.ForeignKey(Manutencao, related_name='ManOleoFiltro', on_delete=models.CASCADE)
    oleoFiltroFK = models.ForeignKey(OleoFiltro, related_name='ManOleoFiltroFK', on_delete=models.CASCADE)

    def __str__(self):
        return self.oleoFiltroFK.oleo

class ManPastilhaDeFreio(models.Model):
    manutencaoFK = models.ForeignKey(Manutencao, related_name='ManPastilhaDeFreio', on_delete=models.CASCADE)
    pastilhaDeFreioFK = models.ForeignKey(PastilhaDeFreio, related_name='ManPastilhaDeFreioFK', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.pastilhaDeFreioFK.pastilha
    
class ManCorreiaDentada(models.Model):
    manutencaoFK = models.ForeignKey(Manutencao, related_name='ManCorreDentada', on_delete=models.CASCADE)
    correiaDentalhaFK = models.ForeignKey(CorreiaDentalha, related_name='ManCorreiaDentalhaFK', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.correiaDentalhaFK.correia_dentalha
    
class ManPneu(models.Model):
    mautencaoFK = models.ForeignKey(Manutencao, related_name='ManPneu', on_delete=models.CASCADE)
    pneuFK = models.ForeignKey(Pneu, related_name='ManPneuFK', on_delete=models.CASCADE)

    def __str__(self):
        return self.pneuFK.pneu
    
class ManFiltroArCondicionado(models.Model):
    manutencaoFK = models.ForeignKey(Manutencao, related_name='ManFiltroArCondicionado', on_delete=models.CASCADE)
    filtroArCondicionadoFK = models.ForeignKey(FiltroArCondicionado, related_name='ManFiltroArCondicionadoFK', on_delete=models.CASCADE)

    def __str__(self):
        return self.filtroArCondicionadoFK.filtro_ar_condicionado

class ManFiltroGas(models.Model):
    mautencaoFK = models.ForeignKey(Manutencao, related_name='ManFiltroGas', on_delete=models.CASCADE)
    filtroGasFK = models.ForeignKey(FiltroGas, related_name='ManFiltroGasFK', on_delete=models.CASCADE)

    def __str__(self):
        return self.filtroGasFK.filtro_gas


class Imposto(models.Model):
    placaImposto = models.CharField(max_length=7)
    licenciamento = models.IntegerField()
    ipva = models.IntegerField()
    seguro = models.IntegerField()
    rastreador = models.IntegerField()
    financiamento = models.IntegerField()
    manutencaoFK = models.ForeignKey(Manutencao, related_name='ImpostoManutencao', on_delete=models.CASCADE)

    def __str__(self):
        return self.placaImposto
    