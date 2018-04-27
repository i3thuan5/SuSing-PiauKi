FROM tai5_gi2-liau7
MAINTAINER sih4sing5hong5

RUN apt-get update
RUN apt-get install -y libboost-all-dev
RUN echo 'from 臺灣言語工具.語言模型.安裝KenLM訓練程式 import 安裝KenLM訓練程式;安裝KenLM訓練程式.安裝kenlm()' | python3
COPY 算語言模型.py 算語言模型.py
RUN cat 台語詞性 | python3 算語言模型.py
RUN cat 詞性.arpa
