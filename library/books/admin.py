from django.contrib import admin
from .models import Author, Book, BookInstance, Genre


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'get_books_count', )
    list_display_links = ('last_name', )


class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    can_delete = False
    extra = 0


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genres', )
    list_filter = ('author', 'genre', )
    inlines = (BookInstanceInline, )


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id', )
    list_filter = ('status', 'due_back', )
    search_fields = ('id', 'book__title', )

    fieldsets = (
        ('Pagrindinė Informacija', {'fields': (
                'id', 
                'book', 
            )}),
        ('Prieinamumas', {'fields': (
                'status', 
                'due_back', 
            )}),
    )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Genre)