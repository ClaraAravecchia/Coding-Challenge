from django.conf.urls import url, include

from . import views
from rest_framework import routers

app_name = "polls"

router = routers.DefaultRouter()
router.register(r'Animal', views.AnimalViewSet)
router.register(r'Veterinario', views.VetViewSet)
router.register(r'Doacoes', views.DoacaoViewSet)

urlpatterns = [
    #Viewsets
    url(r'^$', views.index, name='index'),
    url(r'^animal$', views.Animais, name='Animais'),
    url(r'^veterinario$', views.Vet, name='Vet'),
    url(r'^doacao$', views.Doacao, name='Doacoes'),

    ############ Animais
    #cadastro
    url(r'^cadastro_animal$', views.Cadastro_animal, name="cadastro_animal"),
    url(r'^salva_animal', views.Salva_animal, name="Salva_animal"),

    #Rest
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^listagem', include(router.urls)),
    

    #Edicao
    url(r'^edicao_animal', views.Edicao_animal, name="edicao_animal"),
    url(r'^update_animal', views.Update_animal, name="update_animal"),
    url(r'form_update_animal', views.form_update_animal, name='form_update_animal'),

    #Remocao
    url(r'^remocao_animal', views.Remocao_animal, name="remocao_animal"),
    url(r'^remove_animal', views.Remove_animal, name="remove_animal"),

    ############ Veterinarios
    #cadastro
    url(r'^cadastro_vet$', views.Cadastro_vet, name="cadastro_vet"),
    url(r'^salva_vet', views.Salva_vet, name="Salva_vet"),

    #Edicao
    url(r'^edicao_vet', views.Edicao_vet, name="edicao_vet"),
    url(r'^update_vet', views.Update_vet, name="update_vet"),
    url(r'form_update_vet', views.form_update_vet, name='form_update_vet'),

    #Remocao
    url(r'^remocao_vet', views.Remocao_vet, name="remocao_vet"),
    url(r'^remove_vet', views.Remove_vet, name="remove_vet"),

    ############ Doacoes
    #cadastro
    url(r'^cadastro_doacao$', views.Cadastro_doacao, name="cadastro_doacao"),
    url(r'^salva_doacao', views.Salva_doacao, name="salva_doacao"),

    #edicao
    url(r'^edicao_doacao', views.Edicao_doacao, name="edicao_doacao"),
    url(r'^update_doacao', views.Update_doacao, name="update_doacao"),
    url(r'form_update_doacao', views.form_update_doacao, name='form_update_doacao'),

    #Remocao
    url(r'^remocao_doacao', views.Remocao_doacao, name="remocao_doacao"),
    url(r'^remove_doacao', views.Remove_doacao, name="remove_doacao"),
    

    ## Usr
    url(r'^usuario', views.login, name="login"),
    url(r'^logout', views.logout, name="logout"),
]

