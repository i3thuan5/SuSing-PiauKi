FROM ubuntu:16.04
MAINTAINER sih4sing5hong5

RUN apt-get update -qq
RUN apt-get install -y python3 virtualenv g++ python3-dev git libpq-dev postgresql postgresql-contrib make

# Switch locale
RUN locale-gen zh_TW.UTF-8
ENV LC_ALL zh_TW.UTF-8

RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install Django
RUN pip3 install https://github.com/sih4sing5hong5/tai5-uan5_gian5-gi2_kang1-ku7/archive/%E8%99%95%E7%90%86%E7%BE%85%E9%A6%AC%E5%AD%97%E8%BC%95%E8%81%B2.zip

EXPOSE 10010

COPY . .
RUN python3 manage.py 教典詞性匯入
