from django.test.testcases import TestCase
from 提著詞性結果.views import _查教典詞性資料


class 查詞性(TestCase):
    def test_腔口音(self):
        self.漢字 = '雞'
        self.羅馬字 = 'kue'
        結果 = _查教典詞性資料(self.漢字, self.羅馬字)
        self.assertEqual(結果[0][-1], ['名'])

    def test_又見音(self):
        self.漢字 = '按怎'
        self.羅馬字 = 'án-nuá'
        結果 = _查教典詞性資料(self.漢字, self.羅馬字)
        self.assertEqual(結果[0][-1], ['副'])

    def test_教典編碼(self):
        self.漢字 = '講遐火燒厝矣'
        self.羅馬字 = 'in kóng hia hué-sio-tshù --ah'
        結果 = _查教典詞性資料(self.漢字, self.羅馬字)
        self.assertEqual(結果[0][-1], ['代'])

    def test_兩字輕聲(self):
        self.漢字 = '一寡'
        self.羅馬字 = '--tsi̍t-kuá'
        結果 = _查教典詞性資料(self.漢字, self.羅馬字)
        self.assertEqual(結果[0][-1], ['副'])

    def test_兩字一半輕聲(self):
        self.漢字 = '久來'
        self.羅馬字 = 'kú--lâi'
        結果 = _查教典詞性資料(self.漢字, self.羅馬字)
        self.assertEqual(結果[0][-1], ['副'])

    def test_標點符號(self):
        self.漢字 = '「九月颱，無人知」，'
        self.羅馬字 = '“Káu-gue̍h-thai, bô lâng tsai”,'
        結果 = _查教典詞性資料(self.漢字, self.羅馬字)
        self.assertEqual(結果[0][-1], [])
