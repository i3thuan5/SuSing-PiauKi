
import ssl

from django.test.testcases import TestCase


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 提著詞性結果.views import 物件查程式詞性

ssl.match_hostname = lambda cert, hostname: True


class 查詞性(TestCase):

    def test_詞性(self):
        程式詞性 = 物件查程式詞性(
            拆文分析器.分詞句物件('有｜u7 食｜tsiah8 閣｜koh4 有｜u7 掠｜liah8'),
        )
        self.assertEqual(程式詞性[3], 'V_2')
