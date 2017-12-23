from django.contrib import admin

from .models import About, Contacts


class AboutAdmin(admin.ModelAdmin):
    list_display = ['title']


class ContactsAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone']


admin.site.register(About, AboutAdmin)
admin.site.register(Contacts, ContactsAdmin)
