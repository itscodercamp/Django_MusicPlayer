from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Music_Uploader)
admin.site.register(PlayLists)
