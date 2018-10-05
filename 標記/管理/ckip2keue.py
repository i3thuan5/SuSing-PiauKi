import csv


def _sng():
    tuiing = {}
    with open('詞類比較.csv') as tong:
        for pit, 資料 in enumerate(csv.reader(tong)):
            if pit == 0:
                continue
            ckip詞 = 資料[1].strip()
            keue詞 = 資料[5].strip()
            if ckip詞:
                tuiing[ckip詞] = keue詞
    return tuiing


對應表 = _sng()
