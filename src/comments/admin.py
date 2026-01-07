from django.contrib import admin
from .models import Comment
# Register your models here.

# admin.site.register(Comment)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'content', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at', 'post', 'author')
    search_fields = ('content',)