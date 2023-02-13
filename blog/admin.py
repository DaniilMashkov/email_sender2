from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class DistributionAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'preview', 'status')

