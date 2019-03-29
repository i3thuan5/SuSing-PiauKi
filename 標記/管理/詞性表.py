
from django.contrib import admin


class 詞性表管理(admin.ModelAdmin):
    # change list
    list_display = [
        'id',  '詞性',
        '華文解釋',    '英文解釋'
    ]
    ordering = ['id',  '詞性', ]
    list_per_page = 20
