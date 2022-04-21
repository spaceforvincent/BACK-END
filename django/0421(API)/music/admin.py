from django.contrib import admin
from .models import Artist, Music

# Register your models here.
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Music)
