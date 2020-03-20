#!/usr/bin/python
from django.urls import path
from img_db import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'img_db'
urlpatterns = [
    path('upload/', views.uploadImg, name='upload'),
    path('show/', views.showImg, name='show'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
