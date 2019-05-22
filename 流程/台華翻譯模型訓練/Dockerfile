FROM i3thuan5/tai5-uan5_gian5-gi2_kang1-ku7:tsuan AS MODEL
MAINTAINER i3thuan5

RUN pip3 install --upgrade tai5-uan5_gian5-gi2_kang1-ku7
RUN echo 'from 臺灣言語工具.翻譯.摩西工具.安裝摩西翻譯佮相關程式 import 安裝摩西翻譯佮相關程式; 安裝摩西翻譯佮相關程式.安裝moses(編譯CPU數=4)' | python3

RUn apt-get update && apt-get install -y libpq-dev
RUN pip3 install tai5-uan5_gian5-gi2_hok8-bu7
RUN pip3 install hue7jip8

WORKDIR /opt/
RUN git clone https://github.com/i3thuan5/hok8-bu7.git

WORKDIR /opt/hok8-bu7

RUN pip3 install --upgrade https://github.com/i3thuan5/tai5-uan5_gian5-gi2_kang1-ku7/archive/master.zip
RUN pip3 install 'django<2.1'
RUN python3 manage.py migrate
RUN python3 manage.py 教典例句
RUN python3 manage.py 訓練Moses翻譯做外文 臺語

FROM i3thuan5/tai5-uan5_gian5-gi2_kang1-ku7:latest

COPY --from=MODEL /opt/hok8-bu7/服務資料 /opt/hok8-bu7/服務資料
CMD /usr/local/lib/python3.7/site-packages/外部程式/mosesserver -f /opt/hok8-bu7/服務資料/臺語/翻譯做外文模型/model/moses.ini
