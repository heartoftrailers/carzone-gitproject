from django.contrib import admin
from .models import Team
from django.utils.html import format_html # adding pic. for member team in admin page from hrml tags > lesson 19
# Register your models here.

class TeamAdmin(admin.ModelAdmin): #adming page adding view details about Team lesson 19
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.photo.url))
    
    thumbnail.short_description = 'Photo'
    list_display = ('id','thumbnail','first_name', 'designation', 'created_date')
    list_display_links = ('id','thumbnail','first_name',) # make fields clickable on admin page
    search_fields = ('first_name', 'last_name', 'designation')
    list_filter = ('designation',)

admin.site.register(Team, TeamAdmin) # on order to view these on admin page
