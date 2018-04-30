
import json
from os.path import join, splitext
from posix import listdir
from sys import stdin
from 臺灣言語工具.語言模型.KenLM語言模型 import KenLM語言模型
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.斷詞.語言模型揀集內組 import 語言模型揀集內組
from 臺灣言語工具.語言模型.語言模型 import 語言模型
from 臺灣言語工具.基本物件.詞 import 詞
from 臺灣言語工具.基本物件.組 import 組
from 臺灣言語工具.基本物件.公用變數 import 無音


class 台語斷詞(語言模型):
    def __init__(self):
        self.詞性ngram = KenLM語言模型('詞性.arpa')
        self.詞性語詞機率 = self.讀詞頭尾機率('語詞')
        self.詞性詞頭機率 = self.讀詞頭尾機率('詞頭')
        self.詞性詞尾機率 = self.讀詞頭尾機率('詞尾')
        self.全部詞性 = sorted(self.詞性詞尾機率.keys())

        self.走幾擺 = 0

    def 讀詞頭尾機率(self, 資料夾):
        lm機率 = {}
        for 檔案 in sorted(listdir(資料夾)):
            if 檔案.endswith('.arpa'):
                lm機率[splitext(檔案)[0]] = KenLM語言模型(join(資料夾, 檔案))
        return lm機率

    def 上濟詞數(self):
        return self.詞性ngram.上濟詞數()

    def 評詞陣列分(self, 詞陣列, 開始的所在=0):
        self.走幾擺 += 1
        if self.走幾擺 % 100 == 0:
            print('self.走幾擺', self.走幾擺)
        #         print('詞陣列', file=stderr)
        #         print(詞陣列, file=stderr)
        詞性陣列 = []
        for 詞物件 in 詞陣列:
            try:
                詞性陣列.append(拆文分析器.建立詞物件(詞物件.詞性.replace('V_2', 'VV2')))
            except AttributeError:  # <s>, </s>
                詞性陣列.append(詞物件)
        for 原本詞物件, ngram機率 in zip(詞性陣列[開始的所在:], self.詞性ngram.評詞陣列分(詞性陣列, 開始的所在)):
            干焦型的詞物件 = 詞(原本詞物件.內底字)
            for 字物件 in 干焦型的詞物件.篩出字物件():
                字物件.音 = 無音
            try:
                字頭物件 = 干焦型的詞物件.篩出字物件()[0]
                字尾物件 = 干焦型的詞物件.篩出字物件()[-2]
            except IndexError:
                yield ngram機率
            else:
                語詞機率 = list(self.詞性語詞機率[原本詞物件.詞性].評詞陣列分([干焦型的詞物件]))[0]
                詞頭機率 = list(self.詞性詞頭機率[原本詞物件.詞性].評詞陣列分([詞([字頭物件])]))[0]
                詞尾機率 = list(self.詞性詞尾機率[原本詞物件.詞性].評詞陣列分([詞([字尾物件])]))[0]
#                 print(
#                     原本詞物件, 原本詞物件.詞性, [詞([字頭物件])], [詞([字尾物件])],
#                     ngram機率 + 語詞機率 + 詞頭機率 + 詞尾機率,
#                     ngram機率, 語詞機率, 詞頭機率, 詞尾機率, file=stderr
#                 )
                yield ngram機率 + 語詞機率 + 詞頭機率 + 詞尾機率

    def 斷語句(self, 句物件):
        新句物件 = 拆文分析器.建立句物件('')
        for 詞物件 in 句物件.網出詞物件():
            新集物件 = 拆文分析器.建立集物件('')
            for 詞性 in self.全部詞性[:30]:
                #             for 詞性 in ['Nh', 'D']:
                組物件 = 組([詞物件])
                組物件.網出詞物件()[0].詞性 = 詞性
                組物件.網出詞物件()[0].內底字.append(
                    拆文分析器.建立字物件(詞性.replace('V_2', 'VV2')))
                新集物件.內底組.append(組物件)
            新句物件.內底集.append(新集物件)
        斷詞結果 = 新句物件.揀(語言模型揀集內組, self)
        for 詞物件 in 斷詞結果.網出詞物件():
            詞物件.內底字.pop()
        return 斷詞結果


def main():
    斷詞 = 台語斷詞()
    全部資料 = []
    for 一逝 in stdin.readlines():
        #         句物件 = 拆文分析器.分詞句物件('逐-家｜tak8-ke1 做-伙｜tso3-hue2 來-𨑨-迌｜lai5-tshit4-tho5 ！')
        #         一逝='逐-家｜tak8-ke1 做-伙｜tso3-hue2'
        句物件 = 拆文分析器.分詞句物件(一逝.rstrip())

        句資料 = []
        for 詞物件 in 斷詞.斷語句(句物件).網出詞物件():
            句資料.append({
                '漢字': 詞物件.看型(),
                '臺羅': 詞物件.看音(),
                '詞性': 詞物件.詞性,
            })
        全部資料.append(句資料)
    print(
        json.dumps(全部資料, ensure_ascii=False, sort_keys=True, indent=2)
    )
    print(len(斷詞.全部詞性), 斷詞.全部詞性)


if __name__ == '__main__':
    main()
