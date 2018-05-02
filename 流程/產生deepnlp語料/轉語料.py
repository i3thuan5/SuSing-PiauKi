import json
from sys import stdin
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


def main():
    全部資料 = json.loads(stdin.read())
    with open('train.txt', 'w') as 檔案:
        for 句資料 in 全部資料:
            詞性序列 = []
            for 資料 in 句資料:
                詞性 = 資料['詞性'].split(',')[-1].strip()
                if 詞性 != '':
                    詞物件 = 拆文分析器.對齊詞物件(資料['漢字'], 資料['臺羅'])
                    詞性序列.append('{}/{}'.format(詞物件.看分詞(), 詞性))
                elif len(詞性序列) > 0:
                    print(' '.join(詞性序列), file=檔案)
                    詞性序列 = []


if __name__ == '__main__':
    main()
