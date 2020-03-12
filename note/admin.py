from django.contrib import admin

# Register your models here.
from note.models import Topic, Entry

class TopicAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'quantity', 'character', 'start_time', 'end_time', 'days', 'owner', 'company']
    search_fields = ['text']    # 搜索功能
    list_filter = ['company']    # 过滤器
    list_display_links = ['text']  # 显示链接


class EntryAdmin(admin.ModelAdmin):
    list_display = ['date_added', 'topic', 'company','owner', 'worker', 'footage', 'rock', 'water', 'cement', 'text']
    list_display_links = ['topic']  # 显示链接
    search_fields = ['text']       # 搜索功能
    list_filter = ['topic']  # 过滤器


admin.site.register(Topic, TopicAdmin)
admin.site.register(Entry, EntryAdmin)
