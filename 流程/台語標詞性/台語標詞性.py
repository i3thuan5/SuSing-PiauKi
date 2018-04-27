
from os.path import join, splitext
from posix import listdir
from 臺灣言語工具.語言模型.KenLM語言模型 import KenLM語言模型


class 台語斷詞:
    def __init__(self):
        self.詞性ngram = KenLM語言模型('詞性.arpa')
        self.詞性詞頭機率 = self.讀詞頭尾機率('詞頭')
        self.詞性詞尾機率 = self.讀詞頭尾機率('詞尾')
        self.全部詞性 = set(self.詞性詞尾機率.keys())

    def 讀詞頭尾機率(self, 資料夾):
        lm機率 = {}
        for 檔案 in sorted(listdir(資料夾)):
            if 檔案.endswith('.arpa'):
                lm機率[splitext(檔案)[0]] = KenLM語言模型(join(資料夾, 檔案))
        return lm機率


if __name__ == '__main__':
    斷詞 = 台語斷詞()
    print(斷詞.全部詞性)
