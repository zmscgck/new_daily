from django.contrib import admin
from . models import IMG
# Register your models here.


class IMGAdmin(admin.ModelAdmin):
    list_display = ['date_added', 'img', 'company', 'name', 'owner']
    list_display_links = ['name', 'company']  # 显示链接
    search_fields = ['name']       # 搜索功能
    list_filter = ['date_added', 'company', 'owner']  # 过滤器


admin.site.register(IMG, IMGAdmin)
