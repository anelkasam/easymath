from django.shortcuts import render

from .models import Article


def library_context(request):
    context = {}
    return render(request, 'library_context.tpl', context)
