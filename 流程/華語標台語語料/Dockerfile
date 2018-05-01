FROM su5-sing3
MAINTAINER sih4sing5hong5

RUN echo TAI5TSUAN2HUA2 = \'`/sbin/ip route|awk '/default/ { print $3 }'`\' >> 設定/settings.py
RUN pip3 install --upgrade https://github.com/sih4sing5hong5/tai5-uan5_gian5-gi2_kang1-ku7/archive/master.zip
COPY 台語分詞 台語分詞
COPY 華語標台語語料.py 華語標台語語料.py
RUN cat 台語分詞 | python3 華語標台語語料.py > 台語詞性
RUN cat 台語詞性
