from django.shortcuts import render

from .models import Article


def library_context(request):
    """
    ToDo: Decide what we should show on the main library page.
    Maybe it will be the content of articles in order to public date.
    """
    context = {}
    return render(request, 'library_context.tpl', context)


def definitions(request):
    """
    Return all definitions in alphabetical order
    """
