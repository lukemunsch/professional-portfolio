from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Project

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    """set up how to view models in admin"""
    list_display = (
        'friendly_proj_name',
        'languages',
    )
    ordering = ('project_name',)
    search_fields = ['project_name', 'languages',]


admin.site.register(Project, ProjectAdmin)
