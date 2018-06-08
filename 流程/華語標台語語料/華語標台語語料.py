from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
import os
from sys import stdin, stderr
from 提著詞性結果.國教院 import 物件查國教院詞性


def _main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "設定.settings")
    for 第幾句, 一句 in enumerate(stdin.readlines()):
        if 第幾句 % 100 == 0:
            print('做第 {} 句'.format(第幾句), file=stderr)
        for 句物件 in 拆文分析器.分詞章物件(一句.rstrip()).內底句:
            try:
                國教院詞性, _國教院詞條, _華語句 = 物件查國教院詞性(句物件)
            except Exception:
                pass
            else:
                詞性序列 = []
                for 詞物件, 詞性 in zip(句物件.網出詞物件(), 國教院詞性):
                    詞性序列.append('{}/{}'.format(詞物件.看分詞(), 詞性))
                print(' '.join(詞性序列))


if __name__ == '__main__':
    _main()
