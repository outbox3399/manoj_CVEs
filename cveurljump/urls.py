from django.contrib import admin
from django.urls import include, path, re_path
from . import views
import sys

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    re_path(r'^(.*)/$', views.hello),

]
