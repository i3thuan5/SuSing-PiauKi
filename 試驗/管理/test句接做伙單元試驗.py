from django.contrib.admin.sites import AdminSite
from django.test.testcases import TestCase
from 標記.管理.基礎句選擇 import 基礎句選擇表
from 標記.管理.基礎句選擇 import 基礎句選擇管理


class 句接做伙試驗(TestCase):
    def setUp(self):
        基礎句選擇表.objects.create(原本漢字='', 原本羅馬字='')

    def test_羅數量是著的(self):
        self.fail()

    def test_頭一句的原本內容是三句原本內容接做伙(self):
        self.fail()

    def test_頭一句有揀(self):
        self.fail()

    def test_後壁的句無揀(self):
        self.fail()

    def test_愛連號才有通接(self):
        self.fail()
