from django.shortcuts import get_object_or_404, render

from .models import Article, Definition, Grade, Topic, Subject


def definitions(request):
    """
    Return all definitions in alphabetical order
    """
    context = {
        'definitions': Definition.objects.order_by('name')
    }
    return render(request, 'definitions.html', context)


def subject(request, pk):
    """
    Return all topics and articles
    """
    subject = get_object_or_404(Subject, pk=pk)
    context = {
        'topics': Topic.objects.filter(subject=subject).order_by('title')
    }
    return render(request, 'topics.html', context)


def grade(request, pk):
    """
    Return all topics and articles
    """
    subject = get_object_or_404(Grade, pk=pk)
    context = {
        'topics': Topic.objects.filter(grade=grade).order_by('title')
    }
    return render(request, 'topics.html', context)
