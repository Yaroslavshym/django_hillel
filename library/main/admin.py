from django.contrib import admin

# from library.main import models
from . import models

admin.autodiscover()


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name', 'pseudonym']
    list_display = ('name', 'id', 'pseudonym')
    ordering = ('id',)


class AuthorDetailsAdmin(admin.ModelAdmin):
    search_fields = ['author']
    list_display = ('author',)
    ordering = ('id',)


class BookAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('title', 'price')
    list_filter = ('author',)
    ordering = ('id',)
    readonly_fields = ('created_at',)


class VisitorAdmin(admin.ModelAdmin):
    search_fields = ['name']
    ordering = ('id',)


admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.AuthorDetails, AuthorDetailsAdmin)
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Visitor, VisitorAdmin)
