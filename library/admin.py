from django.contrib import admin

from library.models import Book, Author


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass