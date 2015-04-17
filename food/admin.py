from django.contrib import admin

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo')


class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 0


class ProcedureInline(admin.TabularInline):
    model = Procedure
    extra = 0


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class TweetAdmin(admin.ModelAdmin):
    fields = ['author',
              ('type', 'original_id'),
              'publish_date', 'title', 'logo', 'content',
              ('vote', 'score', 'visit')]
    list_display = ('id', 'title', 'publish_date', 'type', 'original_id')
    list_filter = ['publish_date']
    search_fields = ['title']
    inlines = [IngredientInline, ProcedureInline, CommentInline]


admin.site.register(User, UserAdmin)
admin.site.register(Tweet, TweetAdmin)
admin.site.register(Ingredient)
admin.site.register(Procedure)
admin.site.register(Comment)
admin.site.register(Supplier)