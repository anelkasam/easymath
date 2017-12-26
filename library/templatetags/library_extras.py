from django import template

from library.models import Grade, Subject

register = template.Library()


@register.inclusion_tag('grades.tpl')
def grades():
    return {'grades': Grade.objects.all(),
            'subjects': Subject.objects.all()}
