FROM tai5_gi2-gian5_boo5-hing5
MAINTAINER sih4sing5hong5

RUN pip3 install --upgrade https://github.com/sih4sing5hong5/tai5-uan5_gian5-gi2_kang1-ku7/archive/master.zip
COPY 台語標詞性.py 台語標詞性.py
RUN tail 台語分詞 -n 1 | python3 台語標詞性.py
