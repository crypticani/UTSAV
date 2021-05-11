from django.contrib import admin
from . import models
from django.contrib.sessions.models import Session


admin.site.site_header = "UTSAV Admin"
admin.site.site_title = "UTSAV Admin Portal"
admin.site.index_title = "Welcome to UTSAV admin Portal"


class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']

admin.site.register(models.Profile)
admin.site.register(models.Courses)
admin.site.register(models.ImageGallery)
admin.site.register(models.GalleryFolder)
admin.site.register(Session, SessionAdmin)
admin.site.register(models.Notice)