from django.test.testcases import TestCase
from django.contrib.admin.sites import AdminSite
from 標記.管理.基礎句選擇 import 基礎句選擇表
from 標記.管理.基礎句選擇 import 基礎句選擇管理


class MockRequest(object):
    pass


request = MockRequest()


class 基礎句選擇整合試驗(TestCase):

    def setUp(self):
        self.app_admin = 基礎句選擇管理(基礎句選擇表, AdminSite())

    def test更新揀的時間(self):
        基礎句選擇表.objects.create(原本漢字='一', 原本羅馬字='it')
        queryset = 基礎句選擇表.objects.filter(pk=1)
        self.app_admin.這幾句先標記(request, queryset)
        self.assertIsNotNone(基礎句選擇表.objects.get(pk=1).揀的時間)

    def test莫揀的句更新揀的時間(self):
        基礎句選擇表.objects.create(原本漢字='漢', 原本羅馬字='han')
        queryset = 基礎句選擇表.objects.filter(pk=1)
        self.app_admin.這幾句先莫標記(request, queryset)
        self.assertIsNotNone(基礎句選擇表.objects.get(pk=1).揀的時間)
