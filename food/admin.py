from django.contrib import admin

from .models import *


class UserAdmin(admin.ModelAdmin):
    fields = ['name']


class TweetAdmin(admin.ModelAdmin):
    fields = ['publish_date', 'title', 'logo', 'content', 'visit']


admin.site.register(User, UserAdmin)
admin.site.register(Tweet, TweetAdmin)