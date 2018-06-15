from unittest.mock import patch

from django.test.testcases import TestCase


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 提著詞性結果.國教院 import 物件查國教院詞性


class 查詞性(TestCase):

    def setUp(self):
        self.xmlrpcPatcher = patch('xmlrpc.client.ServerProxy')
        self.xmlrpcMock = self.xmlrpcPatcher.start()
        self.xmlrpcMock.return_value.translate.return_value = {
            'text': '\\u5927\\u5bb6-\\uff08-Nh-\\uff09  \\u4e00\\u8d77-\\uff08-D-\\uff09  \\u4f86-\\U00028468-\\u8fcc\\uff5clai5-tshit4-tho5|UNK|UNK|UNK  \\uff01|UNK|UNK|UNK  ',
            'align': [
                {'src-start': 0, 'src-end': 0, 'tgt-start': 0},
                {'src-start': 1, 'src-end': 1, 'tgt-start': 1},
                {'src-start': 2, 'src-end': 2, 'tgt-start': 2},
                {'src-start': 3, 'src-end': 3, 'tgt-start': 3}],
            'nbest': [{
                'hyp': ' \\u5927\\u5bb6-\\uff08-Nh-\\uff09  \\u4e00\\u8d77-\\uff08-D-\\uff09  \\u4f86-\\U00028468-\\u8fcc\\uff5clai5-tshit4-tho5|UNK|UNK|UNK  \\uff01|UNK|UNK|UNK  ',
                'word-align': [
                    {'source-word': 0, 'target-word': 0},
                    {'source-word': 1, 'target-word': 1},
                    {'source-word': 2, 'target-word': 2},
                    {'source-word': 3, 'target-word': 3}
                ],
                'align': [
                    {'src-start': 0, 'src-end': 0, 'tgt-start': 0},
                    {'src-start': 1, 'src-end': 1, 'tgt-start': 1},
                    {'src-start': 2, 'src-end': 2, 'tgt-start': 2},
                    {'src-start': 3, 'src-end': 3, 'tgt-start': 3}
                ],
                'totalScore': -213.0541534423828
            }]
        }

    def tearDown(self):
        self.xmlrpcPatcher.stop()

    def test_詞性(self):
        國教院詞性, _國教院詞條, _華語型 = 物件查國教院詞性(
            拆文分析器.分詞句物件('逐-家｜tak8-ke1 做-伙｜tso3-hue2 來-𨑨-迌｜lai5-tshit4-tho5 ！'),
        )
        self.assertEqual(國教院詞性, ['Nh', 'D', '', ''])

    def test_詞條(self):
        _國教院詞性, 國教院詞條, _華語型 = 物件查國教院詞性(
            拆文分析器.分詞句物件('逐-家｜tak8-ke1 做-伙｜tso3-hue2 來-𨑨-迌｜lai5-tshit4-tho5 ！'),
        )
        self.assertEqual(國教院詞條, ['大家（Nh）', '一起（D）', '', ''])
