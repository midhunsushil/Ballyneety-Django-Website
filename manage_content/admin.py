from django.contrib import admin
import admin_thumbnails
from .models import *

# Register your models here.

@admin_thumbnails.thumbnail('image')
class PostGalleryInline(admin.TabularInline):
    model = PostGallery
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [PostGalleryInline]

admin.site.register(Page)
admin.site.register(Post, PostAdmin)
