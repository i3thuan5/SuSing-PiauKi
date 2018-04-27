FROM su5-sing3
MAINTAINER sih4sing5hong5

RUN echo TAI5TSUAN2HUA2 = \'`/sbin/ip route|awk '/default/ { print $3 }'`\' >> 設定/settings.py
COPY 台語分詞 台語分詞
COPY 華語標台語語料.py 華語標台語語料.py
RUN cat 台語分詞 | python3 華語標台語語料.py | tee 台語詞性
