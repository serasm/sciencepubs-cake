from django.contrib import admin

from .models import PublicationCategory, Publication

# Register your models here.
class adminPublicationCategory(admin.ModelAdmin):
    list_display = ('PublicationCategoryId', 'PublicationCategoryName')

admin.site.register(PublicationCategory, adminPublicationCategory)
admin.site.register(Publication)