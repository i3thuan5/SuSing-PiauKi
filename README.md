# su5-sing3
台語詞性標記

## 走服務
```
docker-compose up --build
```

## 其他
```
time docker build -t su5-sing3 .
time docker build -t tai5-hua5 流程/台華翻譯模型訓練/
docker run --rm -p 8080:8080 tai5-hua5 /usr/local/lib/python3.5/dist-packages/外部程式/mosesdecoder/bin/mosesserver -f 服務資料/臺語/翻譯做外文模型/model/moses.ini
time docker build -t tai5_gi2-liau7 流程/華語標台語語料/
```