from django.db import models


class Contacts(models.Model):
    """ Contact information """
    email = models.EmailField()
    phone = models.CharField(max_length=12)


class About(models.Model):
    """ The parts of description about service """
    title = models.CharField(max_length=100, verbose_name='Заглавие')
    text = models.TextField(verbose_name='Текст')
