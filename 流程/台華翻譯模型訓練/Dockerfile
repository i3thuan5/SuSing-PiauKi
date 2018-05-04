FROM hok8-bu7
MAINTAINER sih4sing5hong5

RUN pip3 install --upgrade https://github.com/i3thuan5/tai5-uan5_gian5-gi2_hok8-bu7/archive/%E7%BF%BB%E8%AD%AF%E6%94%B9%E9%81%8E%E6%B8%A1.zip
RUN pip3 install --upgrade https://github.com/i3thuan5/tai5-uan5_gian5-gi2_kang1-ku7/archive/master.zip
RUN python3 manage.py migrate
RUN python3 manage.py 教典例句
RUN echo 'from 臺灣言語工具.翻譯.摩西工具.安裝摩西翻譯佮相關程式 import 安裝摩西翻譯佮相關程式; 安裝摩西翻譯佮相關程式.安裝gizapp();' | python3
RUN echo 'from 臺灣言語工具.翻譯.摩西工具.安裝摩西翻譯佮相關程式 import 安裝摩西翻譯佮相關程式; 安裝摩西翻譯佮相關程式.安裝moses(編譯CPU數=4)' | python3

RUN python3 manage.py 訓練Moses翻譯做外文 臺語
#/usr/local/lib/python3.5/dist-packages/外部程式/mosesdecoder/bin/mosesserver -f 服務資料/臺語/翻譯做外文模型/model/moses.ini
