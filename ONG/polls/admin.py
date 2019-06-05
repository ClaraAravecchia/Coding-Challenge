# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Animal, Veterinario, Historico_atendimento, Doacoes

admin.site.register(Animal)
admin.site.register(Veterinario)
admin.site.register(Historico_atendimento)
admin.site.register(Doacoes)