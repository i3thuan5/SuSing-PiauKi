import json
from os import makedirs
from os.path import join
from shutil import copyfile
from sys import stdin
from tempfile import TemporaryDirectory
from 臺灣言語工具.語言模型.KenLM語言模型訓練 import KenLM語言模型訓練
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


def main():
    全部資料 = json.loads(stdin.read())
    詞性檔名 = '詞性.txt'
    語詞 = {}
    詞頭 = {}
    詞尾 = {}
    with open(詞性檔名, 'w') as 檔案:
        for 句資料 in 全部資料:
            詞性序列 = []
            for 資料 in 句資料:
                詞性 = 資料['詞性'].split(',')[-1].strip()
                if 詞性 != '':
                    詞性序列.append(詞性)
                    詞物件 = 拆文分析器.對齊詞物件(資料['漢字'], 資料['臺羅'])
                    字頭物件 = 詞物件.篩出字物件()[0]
                    字尾物件 = 詞物件.篩出字物件()[-1]
                    try:
                        語詞[詞性].append(詞物件.看型('-'))
                    except KeyError:
                        語詞[詞性] = [詞物件.看型('-')]
                    try:
                        詞頭[詞性].append(字頭物件.看型())
                    except KeyError:
                        詞頭[詞性] = [字頭物件.看型()]
                    try:
                        詞尾[詞性].append(字尾物件.看型())
                    except KeyError:
                        詞尾[詞性] = [字尾物件.看型()]
                else:
                    詞性序列.append('UNK')
            print(' '.join(詞性序列), file=檔案)

    with TemporaryDirectory() as 暫存資料夾:
        copyfile(
            KenLM語言模型訓練().訓練([詞性檔名], 暫存資料夾, 連紲詞長度=3),
            '詞性.arpa'
        )
    輸出到資料夾('語詞', 語詞)
    輸出到資料夾('詞頭', 詞頭)
    輸出到資料夾('詞尾', 詞尾)


def 輸出到資料夾(詞頭資料夾, 詞資料):
    makedirs(詞頭資料夾)
    for 詞性, 字陣列 in 詞資料.items():
        檔名 = join(詞頭資料夾, 詞性)
        with open('{}.txt'.format(檔名), 'w') as 檔案:
            print(' '.join(字陣列), file=檔案)
        with TemporaryDirectory() as 暫存資料夾:
            copyfile(
                KenLM語言模型訓練().訓練(['{}.txt'.format(檔名)], 暫存資料夾, 連紲詞長度=2),
                '{}.arpa'.format(檔名)
            )


if __name__ == '__main__':
    main()
