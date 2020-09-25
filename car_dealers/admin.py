from django.contrib import admin
from .models import Car_dealers

class Car_dealersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'date_hired')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    list_per_page = 25

admin.site.register(Car_dealers, Car_dealersAdmin)
