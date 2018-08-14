from django.test.testcases import TestCase
from 標記.管理.基礎句選擇 import 基礎句選擇表
from 標記.templatetags.ki1_tshoo2_ku3_tags import _揀的最新一句
from 標記.管理.基礎句選擇 import 基礎句選擇管理
from django.contrib.admin.sites import AdminSite


class 基礎句選擇Tag單元試驗(TestCase):

    def setUp(self):
        self.app_admin = 基礎句選擇管理(基礎句選擇表, AdminSite())

    # template tag
    def test猶未揀_id是None(self):
        基礎句選擇表.objects.create(原本漢字='漢', 原本羅馬字='han')
        self.assertEqual(_揀的最新一句(), 0)

    def test揀2_id是2(self):
        for 資料 in range(33):
            基礎句選擇表.objects.create(原本漢字=資料, 原本羅馬字=資料, )
        queryset = 基礎句選擇表.objects.filter(pk__in=[2])
        self.app_admin.這幾句先標記(None, queryset)
        self.assertEqual(_揀的最新一句(), 2)

    def test揀23_id是3(self):
        # 1x 2v 3v => 顯示id = 3
        for 資料 in range(33):
            基礎句選擇表.objects.create(原本漢字=資料, 原本羅馬字=資料, )
        queryset = 基礎句選擇表.objects.filter(pk__in=[2, 3])
        self.app_admin.這幾句先標記(None, queryset)
        self.assertEqual(_揀的最新一句(), 3)

    def test莫揀1_id維持3(self):
        # 1v 2v 3v =>
        # 1x 2v 3v => 顯示id = 3
        for 資料 in range(33):
            基礎句選擇表.objects.create(原本漢字=資料, 原本羅馬字=資料, )
        # 先標記123
        queryset = 基礎句選擇表.objects.filter(pk__in=[1, 2, 3])
        self.app_admin.這幾句先標記(None, queryset)
        # 才閣取消1
        queryset = 基礎句選擇表.objects.filter(pk__in=[1])
        self.app_admin.這幾句先莫標記(None, queryset)
        self.assertEqual(_揀的最新一句(), 3)

    def test加莫揀4_id改4(self):
        # 1v 2v 3v =>
        # 1v 2v 3v 4x => 顯示id = 4
        for 資料 in range(33):
            基礎句選擇表.objects.create(原本漢字=資料, 原本羅馬字=資料, )
        # 先標記123
        queryset = 基礎句選擇表.objects.filter(pk__in=[1, 2, 3])
        self.app_admin.這幾句先標記(None, queryset)
        # 才閣取消4
        queryset = 基礎句選擇表.objects.filter(pk__in=[4])
        self.app_admin.這幾句先莫標記(None, queryset)
        self.assertEqual(_揀的最新一句(), 4)

    def test上大3改莫揀_id維持3(self):
        # 1v 2v 3v =>
        # 1v 2v 3x => 顯示id = 3
        for 資料 in range(33):
            基礎句選擇表.objects.create(原本漢字=資料, 原本羅馬字=資料, )
        # 先標記123
        queryset = 基礎句選擇表.objects.filter(pk__in=[1, 2, 3])
        self.app_admin.這幾句先標記(None, queryset)
        # 才閣取消3
        queryset = 基礎句選擇表.objects.filter(pk__in=[3])
        self.app_admin.這幾句先莫標記(None, queryset)
        self.assertEqual(_揀的最新一句(), 3)
