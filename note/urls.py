#!/usr/bin/python
from django.urls import path
# from django.conf.urls import url
from . import views

app_name = 'note'
urlpatterns = [
    path('admin/', views.index, name='admin'),
    path('', views.index, name='index'),
    path('daily/', views.new_daily, name='daily'),
    path('graph/', views.graph, name='graph'),
    path('topics/', views.topics, name='topics'),
    path('entries/', views.entries, name='entries'),
    path('topics/<topic_id>', views.topic, name='topic'),  # 某一单位工程的所有日志
    path('new_topic/', views. new_topic, name='new_topic'),
    path('new_entry/<topic_id>', views.new_entry, name='new_entry'),
    path('new_entries/', views.new_entries, name='new_entries'),
    path('edit_entry/<entry_id>', views.edit_entry, name='edit_entry'),

]
