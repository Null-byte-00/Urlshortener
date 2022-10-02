from django.contrib import admin
from .models import ShortenedUrl
# Register your models here.

@admin.register(ShortenedUrl)
class ShortenedUrlAdmin(admin.ModelAdmin):
    list_display = ['link', 'slug', 'target_url', 'date']
    list_filter = ['date']