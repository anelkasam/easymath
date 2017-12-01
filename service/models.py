from django.db import models


class Contacts(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=12)
