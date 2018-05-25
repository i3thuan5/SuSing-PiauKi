# su5-sing3
[![Build Status](https://travis-ci.org/i3thuan5/su5-sing3.svg?branch=master)](https://travis-ci.org/i3thuan5/su5-sing3)
[![Coverage Status](https://coveralls.io/repos/github/i3thuan5/su5-sing3/badge.svg?branch=master)](https://coveralls.io/github/i3thuan5/su5-sing3?branch=master)

台語詞性標記

## 走服務
```
docker-compose up --build
```

## 其他
```
time docker build -t su5-sing3 .
time docker build -t tai5-hua5 流程/台華翻譯模型訓練/
docker run -d  --name tai5-hua5 -p 8080:8080 tai5-hua5 /usr/local/lib/python3.5/dist-packages/外部程式/mosesdecoder/bin/mosesserver -f 服務資料/臺語/翻譯做外文模型/model/moses.ini
# docker run --rm -p 8080:8080 tai5-hua5 /usr/local/lib/python3.5/dist-packages/外部程式/mosesdecoder/bin/mosesserver -f 服務資料/臺語/翻譯做外文模型/model/moses.ini
time docker build -t tai5_gi2-liau7 流程/華語標台語語料/

# 家己實作，尾仔放棄，直接用人的套件較穩
# time docker build -t tai5_gi2-gian5_boo5-hing5 流程/台語語料算語言模型/
# time docker build -t tai5_tng7-su5 流程/台語標詞性/

time docker build -t tai5_deepnlp 流程/產生deepnlp語料/
```

### 上傳臺語翻華語
```
docker login 
time docker build -t tai5-hua5 流程/台華翻譯模型訓練/
docker tag tai5-hua5 i3thuan5/su5-sing3_tai5-hua5
docker push i3thuan5/su5-sing3_tai5-hua5
```