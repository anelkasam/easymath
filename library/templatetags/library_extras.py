from django import template

from library.models import Grade, Subject

register = template.Library()


@register.inclusion_tag('lib_dropdown.html')
def lib_dropdown():
    return {'grades': Grade.objects.all(),
            'subjects': Subject.objects.all()}
