from django.contrib import admin

# Register your models here.
from .models import Tag,Author,Post

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Tag)