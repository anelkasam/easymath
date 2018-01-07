from django.shortcuts import render
from django.http import HttpResponse

from service.models import About


def index(request):
    context = {'name': 'Elena',
               'about': About.objects.all()}
    return render(request, 'index.html', context)

