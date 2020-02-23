from django.contrib import admin

from .models import Publication
# Register your models here.
class adminPublication(admin.ModelAdmin):
    list_display = ('publicationName', 'publicationIssn', 'publicationEissn')

admin.site.register(Publication,adminPublication)