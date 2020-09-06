from django.contrib import admin

from .models import Client , Comment , VechicleByCust


class CommentInline(admin.TabularInline):
    model = Comment

class VechicleInline(admin.TabularInline):
    model = VechicleByCust

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name' , 'author')
    list_filter =  ('name' , 'author')
    search_fields =  ('name' , 'author')
    ordering = ['name']

    inlines = [
        CommentInline ,
        VechicleInline
    ]

admin.site.register(Client, ClientAdmin)
admin.site.register(Comment)
admin.site.register(VechicleByCust)
