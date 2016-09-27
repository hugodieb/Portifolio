from __future__ import unicode_literals

from django.db import models

# Create your models here.

class DadosPessoais(models .model):
    name = models.CharField (max_length= 50, verbose_name= 'Nome')
    address = models.CharField (max_length= 100, verbose_name= 'Endereco')
    city = models.CharField (max_length= 50, verbose_name= 'Cidade')
    cep = models.CharField (max_length= 50, verbose_name= 'Cep')
    phone = models.CharField (max_length= 50, verbose_name= 'Telefone')

    about = models.TextField  (max_length= 255, verbose_name= 'Sobre')
    data_nascimento = models .CharField (max_length= 50, verbose_name= 'Data de Nascimento')
    email = models.EmailField (max_length= 50, verbose_name= 'Email')

    conhecimentos = models .TextField (max_length= 255, verbose_name= 'Conhecimentos')
    github = models .CharField (max_length= 50, verbose_name= 'GitHub')

    def __str__(self):
        return self .name


