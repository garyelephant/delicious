from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(Tweet)
admin.site.register(Comment)
admin.site.register(Ingredient)
admin.site.register(Procedure)
admin.site.register(Supplier)