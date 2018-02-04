# -*- coding: utf-8 -*-

from csv import DictReader
import io
from urllib.request import urlopen


from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


def 匯入教典內的詞性():
    for 詞物件 in 教典資料.全部資料():
        print(詞物件)


class 教典資料:
    詞目總檔網址 = 'https://github.com/g0v/moedict-data-twblg/raw/master/uni/%E8%A9%9E%E7%9B%AE%E7%B8%BD%E6%AA%94.csv'
    釋義網址 = 'https://raw.githubusercontent.com/g0v/moedict-data-twblg/master/uni/%E9%87%8B%E7%BE%A9.csv'
    詞性對照網址 = 'https://raw.githubusercontent.com/g0v/moedict-data-twblg/master/uni/%E9%87%8B%E7%BE%A9.%E8%A9%9E%E6%80%A7%E5%B0%8D%E7%85%A7.csv'

    @classmethod
    def 全部資料(cls):
        yield from cls._詞目總檔()

    @classmethod
    def _詞目總檔(cls):
        釋義表 = cls._釋義表()
        with urlopen(cls.詞目總檔網址) as 檔:
            with io.StringIO(檔.read().decode()) as 資料:
                for row in DictReader(資料):
                    主編碼 = row['主編碼'].strip()
                    音讀 = row['音讀'].strip()
                    漢字 = row['詞目'].strip()
                    for 一音 in 音讀.split('/'):
                        臺羅 = 一音.strip()
                        整理後漢字 = 文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 漢字)
                        整理後臺羅 = 文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 臺羅)
                        try:
                            yield 整理後漢字, 整理後臺羅, tuple(sorted(釋義表[主編碼]))
                        except KeyError:
                            pass

    @classmethod
    def _釋義表(cls):
        詞性對照表 = cls._詞性對照表()
        資料 = {}
        with urlopen(cls.釋義網址) as 檔:
            with io.StringIO(檔.read().decode()) as 字串資料:
                for row in DictReader(字串資料):
                    主編碼 = row['主編碼'].strip()
                    詞性代號 = row['詞性代號'].strip()
                    詞性 = 詞性對照表[詞性代號]
                    if 詞性 == '不標示':
                        continue
                    try:
                        資料[主編碼].add(詞性)
                    except KeyError:
                        資料[主編碼] = {詞性}
        return 資料

    @classmethod
    def _詞性對照表(cls):
        詞性對照 = {}
        with urlopen(cls.詞性對照網址) as 檔:
            with io.StringIO(檔.read().decode()) as 字串資料:
                for row in DictReader(字串資料):
                    詞性代號 = row['詞性代號'].strip()
                    詞性 = row['正確'].strip()
                    詞性對照[詞性代號] = 詞性
        return 詞性對照
