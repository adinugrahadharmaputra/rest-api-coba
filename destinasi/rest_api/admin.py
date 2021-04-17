from django.contrib import admin
from destinasi.models import Destinasi
# Register your models here.

class DestinasiAdmin(admin, ModelAdmin):
    list_display = ['name', 'description', 'image_url','address','site', 'created','updated']
    search_fields = ['name','description', 'address']
    list_per_page = 5

admin.site.register(Destinasi,DestinasiAdmin)