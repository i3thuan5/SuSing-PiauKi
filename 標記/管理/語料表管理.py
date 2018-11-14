
from django.contrib import admin


class 語料表管理(admin.ModelAdmin):
    list_filter = ['語料狀況', '先標記無', ]
    readonly_fields = ['漢字', ]
    list_per_page = 20

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    class Media:
        css = {
            "all": ("css/admin_gi2_liau7_pio2.css", "css/moedictFont.css")
        }

    def 這幾句kap做伙(self, request, queryset):
        self.model.kap(queryset)
