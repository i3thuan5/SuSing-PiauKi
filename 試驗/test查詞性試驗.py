from django.test.testcases import TestCase
from 提著詞性結果.views import 查教典詞性


class 查詞性(TestCase):
    def tearDown(self):
        查教典詞性(self.漢字, self.羅馬字)

    def test_標點符號(self):
        self.漢字 = '「九月颱，無人知」，'
        self.羅馬字 = '“Káu-gue̍h-thai, bô lâng tsai”,'

    def test_輕聲(self):
        self.漢字 = '你欲來食飯無'
        self.羅馬字 = 'lí beh lâi tsia̍h-pn̄g --bô'
