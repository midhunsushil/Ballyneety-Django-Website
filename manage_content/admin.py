from django.contrib import admin
import admin_thumbnails
from .models import *

# Register your models here.

@admin_thumbnails.thumbnail('image')
class PostGalleryInline(admin.TabularInline):
    model = PostGallery
    extra = 1

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'page')
    list_filter = ('page',)
    inlines = [PostGalleryInline]

@admin_thumbnails.thumbnail('image', 'Thumbnail')
class PostGalleryAdmin(admin.ModelAdmin):
    list_display = ('post', 'image', 'image_thumbnail')

admin.site.register(Page)
admin.site.register(Post, PostAdmin)
admin.site.register(PostGallery, PostGalleryAdmin)
