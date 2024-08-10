from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

admin.site.register(User)
admin.site.register(Foto)
admin.site.register(OleoFiltro)
admin.site.register(PastilhaDeFreio)
admin.site.register(CorreiaDentalha)
admin.site.register(CaboDeVela)
admin.site.register(Pneu)
admin.site.register(FiltroArCondicionado)
admin.site.register(FiltroGas)
admin.site.register(Carro)
admin.site.register(Manutencao)
admin.site.register(ManOleoFiltro)
admin.site.register(ManPastilhaDeFreio)
admin.site.register(ManCorreiaDentada)
admin.site.register(ManPneu)
admin.site.register(ManFiltroArCondicionado)
admin.site.register(ManFiltroGas)
admin.site.register(Imposto)
