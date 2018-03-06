# -*- coding: utf-8 -*-

from csv import DictReader
import io
from urllib.request import urlopen


class 教典造字表資料:
    造字網址 = 'https://github.com/g0v/moedict-data-twblg/raw/master/x-%E9%80%A0%E5%AD%97.csv'

    @classmethod
    def 造字表(cls):
        表 = {}
        with urlopen(cls.造字網址) as 檔:
            with io.StringIO(檔.read().decode()) as 字串資料:
                for row in DictReader(字串資料):
                    造字碼 = row['造字碼'].strip()
                    對應字 = row['對應字'].strip()
                    表[chr(int(造字碼, 16))] = 對應字
        return 表
