from django.contrib import admin
from .models import Post
# Register your models here.

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'content')