from django.contrib import admin
from scraps.models import Technology, Content


admin.site.register(Technology)


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology', 'id')
    list_filter = ('technology',)
