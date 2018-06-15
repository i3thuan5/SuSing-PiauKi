from unittest.mock import patch

from django.test.testcases import TestCase


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 提著詞性結果.國教院 import 物件查國教院詞性


class 查詞性(TestCase):

    def setUp(self):
        self.xmlrpcPatcher = patch('xmlrpc.client.ServerProxy')
        self.xmlrpcMock = self.xmlrpcPatcher.start()
        self.xmlrpcMock.return_value.translate.return_value = {
            'nbest': [{
                'totalScore': -13.03787612915039,
                'word-align': [
                    {'source-word': 1, 'target-word': 0},
                    {'source-word': 2, 'target-word': 1},
                    {'source-word': 3, 'target-word': 2},
                    {'source-word': 4, 'target-word': 3}
                ],
                'align': [
                    {'tgt-start': 0, 'src-start': 0, 'src-end': 1},
                    {'tgt-start': 1, 'src-start': 2, 'src-end': 2},
                    {'tgt-start': 2, 'src-start': 3, 'src-end': 3},
                    {'tgt-start': 3, 'src-start': 4, 'src-end': 4}
                ],
                'hyp': ' \\u5403-\\uff08-VC-\\uff09  \\u9084-\\uff08-D-\\uff09  \\u6709-\\uff08-VV2-\\uff09  \\u6293-\\uff08-VC-\\uff09  '
            }],
            'text': '\\u5403-\\uff08-VC-\\uff09  \\u9084-\\uff08-D-\\uff09  \\u6709-\\uff08-VV2-\\uff09  \\u6293-\\uff08-VC-\\uff09  ',
            'align': [
                {'tgt-start': 0, 'src-start': 0, 'src-end': 1},
                {'tgt-start': 1, 'src-start': 2, 'src-end': 2},
                {'tgt-start': 2, 'src-start': 3, 'src-end': 3},
                {'tgt-start': 3, 'src-start': 4, 'src-end': 4}
            ]
        }

    def tearDown(self):
        self.xmlrpcPatcher.stop()

    def test_詞性(self):
        國教院詞性, _國教院詞條, _華語型 = 物件查國教院詞性(
            拆文分析器.分詞句物件('有｜u7 食｜tsiah8 閣｜koh4 有｜u7 掠｜liah8'),
        )
        self.assertEqual(國教院詞性[3], 'V_2')
