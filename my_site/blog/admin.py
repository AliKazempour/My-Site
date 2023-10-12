from django.contrib import admin

# Register your models here.
from .models import Tag, Author, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date",)
    list_filter = ("title", "author", "date", "tags")
    search_fields = ("title", "author", "tags")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
