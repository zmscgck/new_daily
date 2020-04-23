from django.contrib import admin

# Register your models here.
from note.models import Topic, Entry


# 页面标题
admin.site.site_title = "工程日报"
# 登录页导航条和首页导航条标题
admin.site.site_header = "日报管理"
# 主页标题
admin.site.index_title = "欢迎登陆"


class TopicAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'company', 'quantity',
                    'character', 'start_time', 'end_time', 'days']
    search_fields = ['text', 'company']    # 搜索功能
    list_filter = ['company', 'text']    # 过滤器
    list_display_links = ['text']  # 显示链接


class EntryAdmin(admin.ModelAdmin):
    list_display = ['date_added', 'topic', 'company', 'worker',
                    'footage', 'cement', 'text', 'owner']
    list_display_links = ['topic', 'company']  # 显示链接
    search_fields = ['text']       # 搜索功能
    list_filter = ['date_added', 'company', 'topic']  # 过滤器


admin.site.register(Topic, TopicAdmin)
admin.site.register(Entry, EntryAdmin)
