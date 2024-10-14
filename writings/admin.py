from django.contrib import admin
from .models import Publication

# Register your models here.
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','image', 'date',)
admin.site.register(Publication, PublicationAdmin)