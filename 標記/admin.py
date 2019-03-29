from django.contrib import admin
from 標記.models import 語料狀況表
from 標記.管理.詞性標記 import 標記表
from 標記.管理.詞性標記 import 標記表管理
from 標記.管理.基礎句選擇 import 基礎句選擇表
from 標記.管理.基礎句選擇 import 基礎句選擇管理
from 標記.models import 詞性表
from 標記.管理.詞性表 import 詞性表管理


admin.site.site_header = '詞性標記系統'
admin.site.site_title = '詞性標記系統'
admin.site.site_url = 'https://github.com/i3thuan5/su5-sing3'

admin.site.disable_action('delete_selected')


class 語料狀況表管理(admin.ModelAdmin):
    list_display = ['id', '狀況', '確定會當用', ]
    ordering = ['id']


admin.site.register(語料狀況表, 語料狀況表管理)
admin.site.register(標記表, 標記表管理)
admin.site.register(基礎句選擇表, 基礎句選擇管理)
admin.site.register(詞性表, 詞性表管理)
