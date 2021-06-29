from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','email')
    list_display_links = ('id','name','email')
    search_fields = ('name','email')
    list_per_page = 25

admin.site.register(Contact,ContactAdmin)