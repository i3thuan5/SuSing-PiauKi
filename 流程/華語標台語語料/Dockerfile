FROM su5-sing3
MAINTAINER sih4sing5hong5

RUN echo TAI5TSUAN2HUA2 = \'`/sbin/ip route|awk '/default/ { print $3 }'`\' >> 設定/settings.py
COPY 台語分詞.gz 台語分詞.gz
COPY 華語標台語語料.py 華語標台語語料.py
RUN zcat 台語分詞.gz | python3 華語標台語語料.py | gzip > 台語詞性.gz
