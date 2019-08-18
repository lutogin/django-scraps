from django.contrib import admin
from scraps.models import Technology, Content


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    pass


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology', 'id')
    list_filter = ('technology',)
