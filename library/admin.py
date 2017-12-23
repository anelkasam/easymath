from django.contrib import admin

from .models import *


class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title']


class PackageAdmin(admin.ModelAdmin):
    list_display = ['title']


class GradeAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Grade, GradeAdmin)
admin.site.register(Package, PackageAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Topic)
admin.site.register(Article)
admin.site.register(Assignment)
