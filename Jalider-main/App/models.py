from django.db import models
# Create your models here.

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
    
class Manutencao(models.Model):
    carro_fk = models.CharField(max_length=1220)
    OleoFiltroFK = models.ForeignKey(OleoFiltro, related_name='ManutencaoOleoFiltro', on_delete=models.CASCADE)
    PastilhaDeFreioFK = models.ForeignKey(PastilhaDeFreio, related_name='ManutencaoPastilhaDeFreio', on_delete=models.CASCADE)
    CorreiaDentalhaFK = models.ForeignKey(CorreiaDentalha, related_name='ManutencaoCorreiaDentalha', on_delete=models.CASCADE)
    PneuFK = models.ForeignKey(Pneu, related_name='ManutencaoPneu', on_delete=models.CASCADE)
    FiltroArCondicionadoFK = models.ForeignKey(FiltroArCondicionado, related_name='ManutencaoFiltroArCondicionado', on_delete=models.CASCADE)
    FiltroGasFK = models.ForeignKey(FiltroGas, related_name='ManutencaoFiltroGas', on_delete=models.CASCADE)

