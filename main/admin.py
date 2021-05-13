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


class ProfileA(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'gender', 'course']
    list_filter = ['gender', 'course', 'signup_confirmation']
    search_fields = ['user__username', 'first_name', 'last_name']


class NoticeA(admin.ModelAdmin):
    list_display = ['id', 'content','date', 'is_active']
    list_filter = ['date', 'is_active']
    search_fields = ['id', 'content']


admin.site.register(models.Profile, ProfileA)
admin.site.register(models.Courses)
admin.site.register(models.ImageGallery)
admin.site.register(models.GalleryFolder)
admin.site.register(Session, SessionAdmin)
admin.site.register(models.Notice, NoticeA)