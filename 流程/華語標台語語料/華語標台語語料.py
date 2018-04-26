from 提著詞性結果.views import 物件查國教院詞性
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
import os

from django.conf import settings


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "設定.settings")
    結果 = 物件查國教院詞性(
        getattr(settings, 'TAI5TSUAN2HUA2', None),
        getattr(settings, 'TAI5TSUAN2HUA2PORT', '8080'),
        拆文分析器.分詞句物件('逐-家｜tak8-ke1 做-伙｜tso3-hue2 來-𨑨-迌｜lai5-tshit4-tho5 ！'),
    )
    print(結果)
