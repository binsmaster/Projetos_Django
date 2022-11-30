from django.contrib import admin

from django.contrib.auth.models import User, Group

# Register your models here.

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.site_header = 'TarefasApp Login'
admin.site.site_title = 'Administração TarefasApp'
admin.site.index_title = 'Administração TarefasApp - Aplicações'