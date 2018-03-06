# -*- coding: utf-8 -*-

from csv import DictReader
import io
from urllib.request import urlopen
from itertools import chain


def 匯入教典內的詞性():
    for 詞物件 in 教典資料.全部資料():
        yield 詞物件


class 教典資料:
    詞目總檔網址 = 'https://github.com/g0v/moedict-data-twblg/raw/master/uni/%E8%A9%9E%E7%9B%AE%E7%B8%BD%E6%AA%94.csv'
    又音網址 = 'https://github.com/g0v/moedict-data-twblg/raw/master/uni/%E5%8F%88%E9%9F%B3.csv'
    釋義網址 = 'https://raw.githubusercontent.com/g0v/moedict-data-twblg/master/uni/%E9%87%8B%E7%BE%A9.csv'
    詞性對照網址 = 'https://raw.githubusercontent.com/g0v/moedict-data-twblg/master/uni/%E9%87%8B%E7%BE%A9.%E8%A9%9E%E6%80%A7%E5%B0%8D%E7%85%A7.csv'

    @classmethod
    def 全部資料(cls):
        yield from cls._詞目總檔()

    @classmethod
    def _詞目總檔(cls):
        釋義表 = cls._釋義表()
        又見音表 = cls._又見音表()
        with urlopen(cls.詞目總檔網址) as 檔:
            with io.StringIO(檔.read().decode()) as 資料:
                for row in DictReader(資料):
                    主編碼 = row['主編碼'].strip()
                    音讀 = row['音讀'].strip()
                    漢字 = row['詞目'].strip()
                    try:
                        詞性 = tuple(sorted(釋義表[主編碼]))
                    except KeyError:
                        pass
                    else:
                        try:
                            又音 = 又見音表[主編碼]
                        except KeyError:
                            又音 = []
                        for 臺羅 in chain(音讀.split('/'), 又音):
                            yield 漢字, 臺羅.strip(), 詞性

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

    @classmethod
    def _又見音表(cls):
        資料 = {}
        with urlopen(cls.又音網址) as 檔:
            with io.StringIO(檔.read().decode()) as 字串資料:
                for row in DictReader(字串資料):
                    if row['又音類型(1.又唸作 2.俗唸作 3.合音唸作)'] == '3':
                        continue
                    主編碼 = row['主編碼'].strip()
                    for 一音 in row['又音'].split('/'):
                        try:
                            資料[主編碼].append(一音)
                        except KeyError:
                            資料[主編碼] = [一音]
        return 資料
