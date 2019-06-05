# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
import datetime
from django.utils import timezone

class Animal(models.Model):
    nome_animal = models.CharField('Nome do Animal', max_length=100)
    idade = models.IntegerField(default= 0)
    especie = models.CharField('Espécie', max_length=100)
    raca = models.CharField('Raça', max_length=100)
    observacao = models.CharField('Observação', max_length=300, blank=True)  # como faz pra n ser NOT NULL??-------------
    #img = models.ImageField(upload_to='Images', blank=True)

    def __str__(self):  #retorna pq é uma chave primaria? Mas ja tem o ID q n repete.....
        return self.nome_animal


class Veterinario(models.Model):
    nome_vet = models.CharField('Nome', max_length=100)
    telefone = models.CharField('Telefone', max_length=30)
    crv = models.CharField('CRV', max_length=30)
    endereco = models.CharField('Endereço', max_length=200)

    def __str__(self):
        return self.nome_vet

class Historico_atendimento(models.Model):
    data_consulta = models.DateTimeField('Data da Consulta')

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name='animal')  # se animal for apagado a FK tbm vai ser
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE, verbose_name='veterinário')
    observacao = models.CharField('Observação', max_length=300, blank=True) 

    def __str__(self):
        return self.animal
        

  
class Doacoes(models.Model):
    nome_doador = models.CharField('Nome do Doador', max_length=100)
    tel_doador = models.CharField('Telefone do Doador', max_length=100)

     #N aceita PK blank  :/
    #nome_animal = models.ForeignKey(Animal, on_delete=models.CASCADE, default=None, verbose_name='animal') 

    CHOICE = ((u'racao', u'Ração'), (u'med', u'Medicamentos'),)
    tipo_doacao = models.CharField('Tipo de Doação', max_length=15, choices=CHOICE)
    qntidade = models.IntegerField(default=1)

    def __str__(self):
        return self.nome_doador
   