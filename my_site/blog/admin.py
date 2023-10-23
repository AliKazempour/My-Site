from django.contrib import admin

# Register your models here.
from .models import Tag, Author, Post,Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date",)
    list_filter = ("title", "author", "date", "tags")
    search_fields = ("title", "author", "tags")
    prepopulated_fields = {"slug": ("title",)}

class CommentAdmin(admin.ModelAdmin):
    list_display=("user_name","post")
    search_fields=("user_name","post")

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment,CommentAdmin)