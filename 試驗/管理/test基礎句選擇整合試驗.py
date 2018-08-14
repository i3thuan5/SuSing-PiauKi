from django.test.testcases import TestCase
from 標記.models import 語料表
from django.urls.base import reverse
from django.contrib.admin.helpers import ACTION_CHECKBOX_NAME
from django.contrib.auth.models import User
from django.contrib.admin.sites import AdminSite
from 標記.管理.基礎句選擇 import 基礎句選擇表
from 標記.管理.基礎句選擇 import 基礎句選擇管理
from unittest import mock
from django.utils.datetime_safe import date


class MockRequest(object):
    pass


request = MockRequest()


class 基礎句選擇整合試驗(TestCase):

    def setUp(self):
        self.app_admin = 基礎句選擇管理(基礎句選擇表, AdminSite())

    def test初始揀的時間(self):
        一語料 = 基礎句選擇表.objects.create(原本漢字='一', 原本羅馬字='it')
        self.assertEqual(一語料.揀的時間, None)
    
    def test更新揀的時間(self):
        一語料 = 基礎句選擇表.objects.create(原本漢字='一', 原本羅馬字='it')
        queryset = 基礎句選擇表.objects.filter(pk=1)
        self.app_admin.這幾句先標記(request, queryset)
        self.assertIsNotNone(基礎句選擇表.objects.get(pk=1).揀的時間)


# class 基礎句選擇整合試驗(TestCase):
#     def setUp(self):
# #         me = User.objects.create_user(username='testclient', password='password')
# #         self.client.force_login(me)
#         password = 'mypassword' 
#         my_admin = User.objects.create_superuser('myuser', 'myemail@test.com', password)
#         self.client.login(username=my_admin.username, password=password)
#         
#     def test揀的句子更新揀的時間(self):
#         一語料 = 語料表.objects.create(原本漢字='一', 原本羅馬字='it')
#         舊的時間 = 一語料.揀的時間
#         print('一料=', 一語料.__dict__)
#         changelist_url = reverse('admin:標記_基礎句選擇表_changelist')
#         print('changelist_url=', changelist_url)
#         data = {
#             'action': '這幾句先標記',
#             ACTION_CHECKBOX_NAME: [str(一語料.pk)]
#         }
#         response = self.client.post(changelist_url, data)
#         print('response=', response)
#         新的時間 = 一語料.揀的時間
#         self.assertNotEqual(舊的時間, 新的時間)
#      
#     def test莫揀的句更新揀的時間(self): 
#         self.fail()
# 
#     # 幫助學姊紀錄最後一次揀的句子做進度
#     def test顯示揀的id是2(self):
#         self.fail()
#         
#     def test揀多句的最新id是3(self):
#         # 1x 2v 3v => 顯示id = 3
#         self.fail()
# 
#     def test改做莫揀了後最新id是3(self):
#         # 1v 2v 3v => 1v 2x 3v => 顯示id = 3
#         self.fail()
