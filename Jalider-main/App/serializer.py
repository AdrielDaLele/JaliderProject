from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        many = True

class FotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foto
        fields = '__all__'
        many = True

class OleoFiltroSerializer(serializers.ModelSerializer):
    class Meta:
        model = OleoFiltro
        fields = '__all__'
        many = True

class PastilhaDeFreioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PastilhaDeFreio
        fields = '__all__'
        many = True

class CorreiaDentalhaSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = CorreiaDentalha
        fields = '__all__'
        many = True

class CaboDeVelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaboDeVela
        fields = '__all__'
        many = True

class PneuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pneu
        fields = '__all__'
        many = True

class CaboDeVelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaboDeVela
        fields = '__all__'
        many = True

class FiltroArCondicionadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FiltroArCondicionado
        fields = '__all__'
        many = True


class FiltroGasSerializer(serializers.ModelSerializer):
    class Meta:
        model = FiltroGas
        fields = '__all__'
        many = True


class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = '__all__'
        many = True


class ManutencaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manutencao
        fields = '__all__'
        many = True


class ManOleoFiltroSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManOleoFiltro
        fields = '__all__'
        many = True


class ManPastilhaDeFreioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManPastilhaDeFreio
        fields = '__all__'
        many = True


class ManPneuSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManPneu
        fields = '__all__'
        many = True

class ManFiltroArCondicionadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManFiltroArCondicionado
        fields = '__all__'
        many = True

class ManFiltroGasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManFiltroGas
        fields = '__all__'
        many = True

class ImpostoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imposto
        fields = '__all__'
        many = True