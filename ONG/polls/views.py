# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *

from django.shortcuts import get_object_or_404

from .serializers import AnimalSerializer, VetSerializer, DoacoesSerializer

from rest_framework import viewsets

from django.conf import settings


# Create your views here.
def index(request):
    #Pagina principal
    return render(request, 'polls/index.html')

def Animais(request):
    #Pagina de Animais
    return render(request, 'polls/animal.html')

def Vet(request):
    #Pagina de Veterinarios
    return render(request, 'polls/veterinario.html')

def Doacao(request):
    #Pagina de Doacoes
    return render(request, 'polls/doacoes.html')

#### Classes pro Rest-Framework
class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all() # vai mostrar toda essa tabela
    serializer_class = AnimalSerializer

class VetViewSet(viewsets.ModelViewSet):
    queryset = Veterinario.objects.all()
    serializer_class = VetSerializer

class DoacaoViewSet(viewsets.ModelViewSet):
    queryset = Doacoes.objects.all()
    serializer_class = DoacoesSerializer



##################################################### Usr
def login(request):
    #Verifica se usuario e senha do POST confere com o usuario e senha de settings.py
    
    usr   = settings.DATABASES['default']['USER']
    senha = settings.DATABASES['default']['PASSWORD']

    if usr == request.POST['usuario'] and senha == request.POST['senha']:
            request.session['user_id'] = usr
            return render(request, 'polls/index.html', {'permissao': permissao(request)})
    else:
        return HttpResponse("Usuário e senha não conferem<br/><a href='../'>Voltar</a>")

def permissao(request):
    #Verifica se a sessao do usuario está ativa
    if request.session['user_id'] == settings.DATABASES['default']['USER']:
        print "permi"
        return True
    else: return False

def logout(request):
    #Exclui o usuario de user_id

    if request.session['user_id'] == settings.DATABASES['default']['USER']:
        request.session['user_id'] = None
        return render(request, 'polls/index.html')
    else:
        return HttpResponse("Você não fez login.<a href='../'>Fazer login</a>")  ###ainda n ta bom



#####################################################  Animal

def Cadastro_animal(request):
    #Chama a pagina de cadastro
    if permissao(request):
        return render(request, 'polls/cadastro_animal.html', {'permissao': permissao(request)})
    else:
        return HttpResponse("Você precisa fazer <a href='../'>login</a> antes de acessar este conteúdo")
    
     
def Salva_animal(request):
    #Salva os dados no DB
        if request.method == "POST":
            nome = request.POST.get('nome', '')
            idade = request.POST.get('idade', '')
            especie = request.POST.get('especie', '')
            raca = request.POST.get('raca', '')
            obs = request.POST.get('observacao', '')
            animal_obj = Animal(nome_animal=nome, idade=idade,
                especie=especie, raca=raca, observacao=obs)
            animal_obj.save()
            return HttpResponse("Animal cadastrado com sucesso<br/><a href='animal'>Voltar</a>")
            
       

def Edicao_animal(request):
    #chama a pag html com o form pra escolher qual animal editar
    if permissao(request):
        return render(request, 'polls/edicao_animal.html',  
        {"animal": Animal.objects.all(), "permissao": permissao(request)})  #primeiro eu tenho q saber q animal editar
    else: 
        return HttpResponse("Você precisa fazer <a href='../'>login</a> antes de acessar este conteúdo")

def form_update_animal(request):
    #chama o html para a edicao de um animal especifico
    selected = str(request.POST.get('animal_selected', ''))
    print type(selected)
    animal = Animal.objects.get(pk=selected)
    return render(request, 'polls/form_update_animal.html',  
    {'animal': animal, "vet": Veterinario.objects.all()})

def Update_animal(request):
    #atualiza o DB
    selected = str(request.POST.get('animal_selected', ''))
    animal = Animal.objects.get(pk=selected)
    nome = request.POST.get('nome', '')
    idade = request.POST.get('idade', '')
    especie = request.POST.get('especie', '')
    raca = request.POST.get('raca', '')
    obs = request.POST.get('observacao', '')
    animal_obj = Animal(pk=selected,nome_animal=nome, idade=idade,      # IDADE N FUNCIONA :/
                especie=especie, raca=raca, observacao=obs)
    animal_obj.save()

    try:
        #pro caso de a edicao for só pro animal e n pra consulta
        consulta     = request.POST.get('data', '')
        vet          = request.POST.get('vet_selected', '')
        obs_consulta = request.POST.get('obs', '')

        vet = Veterinario(pk=vet)           # Instancia de Vet :p
        hist_obj = Historico_atendimento(data_consulta=consulta, animal= animal, 
        veterinario=vet, observacao=obs_consulta)

        hist_obj.save()
    except:
        pass
    return HttpResponse("Animal editado com sucesso<br/><a href='animal'>Voltar</a>")
    


def Remocao_animal(request):
    #Primeiro eu tenho q saber q animal remover
    if permissao(request):
        return render(request, 'polls/remocao_animal.html',
      {"animal": Animal.objects.all(), "permissao": permissao(request)})  
    else: 
        return HttpResponse("Você precisa fazer <a href='../'>login</a> antes de acessar este conteúdo")

def Remove_animal(request):
    #atualiza o DB
    selected = str(request.POST.get('animal_selected', ''))
    animal = Animal.objects.get(pk=selected)
    if request.method == 'POST':
        animal.delete()
        return HttpResponse("Animal removido com sucesso<br/><a href='animal'>Voltar</a>")



###############################################   Veterinario

def Cadastro_vet(request):
    if permissao(request):
        return render(request, 'polls/cadastro_vet.html', {"permissao": permissao(request)})
    else: return HttpResponse("Você precisa fazer <a href='../'>login</a> antes de acessar este conteúdo")
    
     
def Salva_vet(request):
        if request.method == "POST":
            nome_vet = request.POST.get('nome', '')
            telefone = request.POST.get('telefone', )
            crv = request.POST.get('crv', '')
            endereco = request.POST.get('endereco', '')
            
            vet_obj = Veterinario(nome_vet=nome_vet, telefone=telefone,
            crv=crv, endereco=endereco)
            vet_obj.save()
            return HttpResponse("Veterinário cadastrado com sucesso<br/><a href='veterinario'>Voltar</a>")
        

def Edicao_vet(request):
    #chama a pag html com o form pra escolher qual animal editar
    if permissao(request):
        return render(request, 'polls/edicao_vet.html',
      {"vet": Veterinario.objects.all(), "permissao": permissao(request)})  #primeiro eu tenho q saber q vet editar
    else: 
        return HttpResponse("Você precisa fazer <a href='../'>login</a> antes de acessar este conteúdo")

def form_update_vet(request):
    #chama o html para a edicao de um vet especifico
    selected = str(request.POST.get('vet_selected', ''))
    vet = Veterinario.objects.get(pk=selected)
    return render(request, 'polls/form_update_vet.html',  
    {'vet': vet})

def Update_vet(request):
    #atualiza o DB
    selected = str(request.POST.get('vet_selected', ''))
    animal = Veterinario.objects.get(pk=selected)

    nome = request.POST.get('nome', '')
    telefone = request.POST.get('telefone', )
    crv = request.POST.get('crv', '')
    endereco = request.POST.get('endereco', '')

    vet_obj = Veterinario(pk=selected,nome_vet=nome, 
                telefone=telefone, crv=crv, endereco=endereco)
    vet_obj.save()
    return HttpResponse("Veterinário editado com sucesso<br/><a href='veterinario'>Voltar</a>")
    

def Remocao_vet(request):
    if permissao(request):
        return render(request, 'polls/remocao_vet.html',
      {"vet": Veterinario.objects.all(), "permissao": permissao(request)})  #primeiro eu tenho q saber q vet remover
    else: return HttpResponse("Você precisa fazer <a href='../'>login</a> antes de acessar este conteúdo")
def Remove_vet(request):
    #atualiza o DB
    selected = str(request.POST.get('vet_selected', ''))
    vet = Veterinario.objects.get(pk=selected)
    if request.method == 'POST':
        vet.delete()
        return HttpResponse("Veterinário removido com sucesso<br/><a href='veterinario'>Voltar</a>")




########################## Doacoes

###### Cadastro
def Cadastro_doacao(request):
    if permissao(request):
        return render(request, 'polls/cadastro_doacao.html', {"permissao": permissao(request)})
    else: return HttpResponse("Você precisa fazer <a href='../'>login</a> antes de acessar este conteúdo")

     
def Salva_doacao(request):
        if request.method == "POST":
            nome = request.POST.get('nome', '')
            tel = request.POST.get('tel', )
            tipo = request.POST.get('tipo', '')
            qntidade = request.POST.get('qntidade', '')
            
            doacao_obj = Doacoes(nome_doador=nome, 
                tel_doador=tel, tipo_doacao=tipo, qntidade=qntidade)
            doacao_obj.save()
            return HttpResponse("Doacao cadastrada com sucesso<br/><a href='doacao'>Voltar</a>")


####### Edicao

def Edicao_doacao(request):
    #chama a pag html com o form pra escolher qual animal editar
    if permissao(request):
        return render(request, 'polls/edicao_doacao.html',
      {"doacao": Doacoes.objects.all(), "permissao": permissao(request)})  #primeiro eu tenho q saber q vet editar
    else: 
        return HttpResponse("Você precisa fazer <a href='../'>login</a> antes de acessar este conteúdo")

def form_update_doacao(request):
    #chama o html para a edicao de um vet especifico
    selected = str(request.POST.get('doacao_selected', ''))
    doacao = Doacoes.objects.get(pk=selected)
    return render(request, 'polls/form_update_doacao.html',  
    {'doacao': doacao})

def Update_doacao(request):  
    #atualiza o DB
    selected = str(request.POST.get('doacao_selected', ''))
    nome = request.POST.get('nome', '')
    tel = request.POST.get('tel', )
    tipo = request.POST.get('tipo', '')
    qntidade = request.POST.get('qntidade', '')
    
    doacao_obj = Doacoes(pk=selected, nome_doador=nome, 
        tel_doador=tel, tipo_doacao=tipo, qntidade=qntidade)
    doacao_obj.save()
    return HttpResponse("Doacao editada com sucesso<br/><a href='doacao'>Voltar</a>")       

##### Remocao
def Remocao_doacao(request):
    if permissao(request):
        return render(request, 'polls/remocao_doacao.html',
      {"doacao": Doacoes.objects.all(), "permissao": permissao(request)})  #primeiro eu tenho q saber q vet remover
    else: 
        return HttpResponse("Você precisa fazer <a href='../'>login</a> antes de acessar este conteúdo")

def Remove_doacao(request):
    #atualiza o DB
    selected = str(request.POST.get('doacao_selected', ''))
    doacao = Doacoes.objects.get(pk=selected)
    if request.method == 'POST':
        doacao.delete()
        return HttpResponse("Doação removida com sucesso<br/><a href='doacao'>Voltar</a>")