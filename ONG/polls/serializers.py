from .models import Animal, Veterinario, Doacoes

from rest_framework import serializers


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ('nome_animal', 'idade', 'especie', 'raca', 'observacao')

class VetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veterinario
        fields = ('nome_vet', 'telefone', 'crv', 'endereco')

class DoacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doacoes
        fields = ('nome_doador', 'tel_doador', 'tipo_doacao', 'qntidade')

    