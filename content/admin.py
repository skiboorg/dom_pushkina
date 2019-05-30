from django.contrib import admin
from .models import *


class PhotosMembersInline (admin.TabularInline):
    model = Photo
    readonly_fields = ('image_tag',)
    extra = 0


class PhotoAlbumAdmin(admin.ModelAdmin):

    list_display = [field.name for field in PhotoAlbum._meta.fields]
    inlines = [PhotosMembersInline]
    readonly_fields = ('album_cover',)
    exclude = ['name_slug']

    class Meta:
        model = PhotoAlbum


admin.site.register(News)
admin.site.register(PhotoAlbum, PhotoAlbumAdmin)
admin.site.register(Photo)
admin.site.register(callBack)