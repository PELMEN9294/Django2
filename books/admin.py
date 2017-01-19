from django.contrib import admin
from .models import Publisher, Author, Book
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'telephone')
    search_fields = ('first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher')
    list_filter = ('publication_date',)
    date_hierarchy = ('publication_date')
    ordering = ('-publication_date',)
    fields = ('title', 'authors', 'publisher', 'publication_date')

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'country',)
    search_fields = ('name', 'country')



admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)