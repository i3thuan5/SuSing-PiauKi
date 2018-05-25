FROM ubuntu:16.04
MAINTAINER sih4sing5hong5

RUN apt-get update -qq
RUN apt-get install -y python3 virtualenv g++ python3-dev git libpq-dev postgresql postgresql-contrib make

# Switch locale
RUN locale-gen zh_TW.UTF-8
# ENV LANG zh_TW.UTF-8
ENV LC_ALL zh_TW.UTF-8

RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install Django whitenoise gunicorn
RUN pip3 install tai5-uan5_gian5-gi2_kang1-ku7

EXPOSE 8000

RUN mkdir /usr/local/su5-sing3
WORKDIR /usr/local/su5-sing3
COPY . .
RUN mkdir tsu-liāu
RUN sed "s/os.path.join(BASE_DIR, 'db.sqlite3')/os.path.join(BASE_DIR, 'tsu-liāu', 'db.sqlite3')/g" -i 設定/settings.py 
RUN python3 manage.py 教典造字表匯入
RUN python3 manage.py 教典詞性匯入
RUN echo TAI5TSUAN2HUA2 = \'huan1ik8\' >> 設定/settings.py

RUN python3 manage.py migrate
RUN python3 manage.py 匯常見的語料狀況
RUN python3 manage.py 匯新北市150句
RUN python3 manage.py collectstatic
