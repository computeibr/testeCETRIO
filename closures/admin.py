from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models

from .models import DocumentType, Origin, Status, ClosureType, Neighborhood, Ap, Closing

@admin.register(DocumentType)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Origin)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Status)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(ClosureType)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Neighborhood)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Ap)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Closing)
class ClosingAdmin(admin.ModelAdmin):
    list_display = ('id', 'year','year', 'ordinance_number', 'status')
    search_fields = ['process_number', 'street']

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

