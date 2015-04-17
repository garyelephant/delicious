from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^food/', include('food.urls', namespace="food")),
    url(r'^admin/', include(admin.site.urls)),
]
