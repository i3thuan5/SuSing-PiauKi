import json
from json.decoder import JSONDecodeError

from django.contrib import admin
from django.db import models
from django.forms.widgets import CheckboxSelectMultiple, Textarea
from django.utils.timezone import now


from 標記.models import 語料表
from 提著詞性結果.views import 查教典詞性
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 提著詞性結果.views import 物件查程式詞性
from 標記.models import 詞性表
from 提著詞性結果.國教院 import 查國教院詞性
from 標記.管理.ckip2keue import 對應表
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤


class 標記表(語料表):

    def save(self, *args, **kwargs):
        self.標記時間 = now()
        super().save(*args, **kwargs)

    class Meta:
        proxy = True
        verbose_name = "標記表"
        verbose_name_plural = verbose_name


class 標記表管理(admin.ModelAdmin):
    # change list
    list_display = [
        'id', '先標記無', '狀況',
        '漢字', '羅馬字', '詞性',
        '備註',
        '標記時間',
    ]
    ordering = ['-先標記無', '標記者', 'id', ]
    list_filter = ['語料狀況', '先標記無', ]
    readonly_fields = ['漢字', ]
    search_fields = [
        'id', '漢字', '羅馬字', '詞性', '備註',
    ]
    list_per_page = 20

    fieldsets = (
        ('漢字', {
            'fields': ('漢字', '羅馬字', '詞性', '備註', ),
            'classes': ['wide']
        }),
        ('語料狀況', {
            'fields': ('語料狀況', ),
            'classes': ['wide']
        }),
    )

    # 文字欄位顯示從textarea改成input
    # 多對多欄位改用複選
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={
            'rows': 2,
            'column': 40,
            'style': 'resize: none; min-width: 80%; overflow:hidden;'})},
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

    def save_model(self, request, obj, form, change):
        # 儲存標記者
        obj.標記者 = request.user
        super(標記表管理, self).save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    # change view
    # venv/lib/python3.5/site-packages/django/contrib/admin/templates/admin/
#     change_list_template = 'admin/custom_change_list.html'
    change_form_template = 'admin/標記/custom_change_form.html'

    class Media:
        css = {
            "all": ("css/admin_gi2_liau7_pio2.css", "css/moedictFont.css")
        }

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        物件 = self.get_queryset(request).get(id=object_id)
        漢字 = 物件.漢字
        羅馬字 = 物件.羅馬字
        try:
            漢, 羅, 性, 國教院詞性, 國教院詞條, 翻譯華語句, 原程式詞性, 程式詞性 = self.tshue_susing(
                漢字, 羅馬字
            )
            try:
                預設詞性 = json.loads(物件.詞性)
            except JSONDecodeError:
                預設詞性 = 程式詞性
            if len(預設詞性)>len(程式詞性):
                預設詞性=預設詞性[:len(程式詞性)]
            if len(預設詞性)<len(程式詞性):
                預設詞性+=程式詞性[len(預設詞性)-len(程式詞性):]
            extra_context.update({
                '漢': 漢,
                '羅': 羅,
                '性': 性,
                '國教院詞性': 國教院詞性,
                '國教院詞條': 國教院詞條,
                '國教院翻譯華語句': 翻譯華語句,
                '原程式詞性': 原程式詞性,
                '程式詞性': 程式詞性,
                '詞性種類': 詞性表.全部(),
                '預設詞性': 預設詞性,
            })
        except 解析錯誤:
            Hantng = len(拆文分析器.建立句物件(漢字).篩出字物件())
            Lotng = len(拆文分析器.建立句物件(羅馬字).篩出字物件())
            print(物件.詞性)
            try:
                預設詞性 = json.loads(物件.詞性)
            except JSONDecodeError:
                預設詞性 = []
            extra_context.update({
                '錯誤資訊': '漢、羅長度無仝！漢字加標點數量：{}，羅馬字加標點數量：{}'.format(Hantng, Lotng),
                '詞性種類': 詞性表.全部(),
                '預設詞性': 預設詞性,
            })
        return super(標記表管理, self).change_view(request, object_id, form_url, extra_context=extra_context)

    def tshue_susing(self, 漢字, 羅馬字):
        漢, 羅, 性 = 查教典詞性(漢字, 羅馬字)
        句物件 = (
            拆文分析器
            .對齊句物件(漢字, 羅馬字)
            .轉音(臺灣閩南語羅馬字拼音)
        )
        國教院詞性, 國教院詞條, 翻譯華語句 = 查國教院詞性(漢字, 羅馬字)
        原程式詞性 = 物件查程式詞性(句物件)
        程式詞性 = []
        for su in 原程式詞性:
            程式詞性.append(對應表[su])
        return 漢, 羅, 性, 國教院詞性, 國教院詞條, 翻譯華語句, 原程式詞性, 程式詞性
