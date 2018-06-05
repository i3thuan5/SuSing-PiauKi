from 提著詞性結果.views import 物件查國教院詞性
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
import json
import os
from sys import stdin


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "設定.settings")
    全部資料 = []
    for 一句 in stdin.readlines():
        句物件 = 拆文分析器.分詞句物件(一句.rstrip())
        try:
            國教院詞性, _國教院詞條, _華語句 = 物件查國教院詞性(句物件)
        except:
            pass
        else:
          句資料 = []
          for 詞物件, 詞性 in zip(句物件.網出詞物件(), 國教院詞性):
            句資料.append({
                '漢字': 詞物件.看型(),
                '臺羅': 詞物件.看音(),
                '詞性': 詞性,
            })
          全部資料.append(句資料)
    print(
        json.dumps(全部資料, ensure_ascii=False, sort_keys=True, indent=2)
    )
