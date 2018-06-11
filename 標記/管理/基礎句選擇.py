
from django.contrib import admin


from 標記.models import 語料表
from 標記.管理.ReadOnlyAdminFields import ReadOnlyAdminFields


class 基礎句選擇表(語料表):

    class Meta:
        proxy = True
        verbose_name = "基礎句選擇"
        verbose_name_plural = verbose_name


class 基礎句選擇管理(ReadOnlyAdminFields, admin.ModelAdmin):
    list_display = [
        'id',
        '漢字', '羅馬字',
        '備註',
        'perplexity',
    ]
    ordering = ['-perplexity', 'id', ]
    list_filter = ['語料狀況', ]
    readonly_fields = ['漢字', '羅馬字', ]
    search_fields = [
        'id', '漢字', '羅馬字',
    ]
    list_per_page = 20

    fieldsets = (
        ('漢字', {
            'fields': ('漢字', '羅馬字', '詞性', '備註', ),
            'classes': ['wide']
        }),
    )

    def has_add_permission(self, request):
        # 薛：只能由程式上傳音檔和語料
        # 薛：任何人都不能從後台新增
        return True
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    class Media:
        css = {
            "all": ("css/admin_gi2_liau7_pio2.css", "css/moedictFont.css")
        }
