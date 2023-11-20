from rest_framework import serializers
from .models import Firms , Cact719,Empl

class GenerateDocxSerializer(serializers.Serializer):
    num_act = serializers.IntegerField()
    kpp = serializers.CharField()
    inn = serializers.CharField()
    nameZaivitel = serializers.CharField()
    adress = serializers.CharField()
    OGRN = serializers.CharField()


class NumAct(serializers.Serializer):
    number = serializers.CharField()


class CreateAct(serializers.ModelSerializer):
    numbact = serializers.IntegerField()
    class Meta:
        model = Cact719
        fields = ['numbact','dateact']


class SaveActsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cact719
        fields = ['numbact' ,
                  'custexp_inn' ,
                  'custexp_kpp' ,
                  'custexp_ogrn',
                  'custexp_addr',
                  'custexp_namef',
                  'custexp_addr_pa',]

class Firm(serializers.ModelSerializer):
    class Meta:
        model = Firms
        fields = '__all__'

class Acts(serializers.ModelSerializer):
    class Meta:
        model = Cact719
        fields = '__all__'

class EmplSe(serializers.ModelSerializer):
    class Meta:
        model = Empl
        fields = '__all__'


