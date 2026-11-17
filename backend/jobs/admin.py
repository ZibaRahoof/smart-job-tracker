

# Register your models here.
from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'status', 'user', 'created_at')
    list_filter = ('status',)
    search_fields = ('title', 'company')