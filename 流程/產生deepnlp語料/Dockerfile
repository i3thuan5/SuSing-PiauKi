FROM deepnlp
MAINTAINER sih4sing5hong5

RUN pip3 install https://github.com/sih4sing5hong5/tai5-uan5_gian5-gi2_kang1-ku7/archive/master.zip
COPY --from=tai5_gi2-liau7 /usr/local/su5-sing3/台語詞性 台語詞性
COPY 轉語料.py 轉語料.py
RUN cat 台語詞性 | python3 轉語料.py

RUN mkdir deepnlp/pos/data/tw
RUN cat train.txt | head -n -1000 | head -n -1000 > deepnlp/pos/data/tw/train.txt
RUN cat train.txt | head -n -1000 | tail -n 1000 > deepnlp/pos/data/tw/dev.txt
RUN cat train.txt | tail -n 1000 > deepnlp/pos/data/tw/test.txt

WORKDIR /usr/local/deepnlp/deepnlp/pos
# RUN pip3 install tensorflow==1.4.0
RUN cp data/tw/train.txt data/tw/dev.txt
RUN cp data/tw/dev.txt data/tw/test.txt
RUN python3 pos_model.py tw

WORKDIR /usr/local/deepnlp
COPY --from=tai5_gi2-liau7 /usr/local/su5-sing3/台語分詞 台語分詞
COPY 標詞性.py 標詞性.py
# RUN cat /usr/local/deepnlp/deepnlp/pos/data/tw/test.txt | sed 's/\/[^ ]* / /g' | tail | python3 標詞性.py
RUN cat 台語分詞 | tail | python3 標詞性.py
