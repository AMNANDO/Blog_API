from django.contrib import admin
from .models import Like
# Register your models here.

# admin.site.register(Like)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'created_at')
    list_filter = ('post', 'user', 'created_at')
    # search_fields = ['user', 'post']