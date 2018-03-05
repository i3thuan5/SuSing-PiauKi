import json

from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.context import RequestContext


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


def 查詞性(request):
    漢字 = request.GET['漢字']
    羅馬字 = request.GET['羅馬字']

    return JsonResponse({'詞性': 查教典詞性(漢字, 羅馬字)})


def 查詞性頁(request):
    try:
        漢字 = request.GET['漢字']
        羅馬字 = request.GET['羅馬字']
    except:
        漢字 = ''
        羅馬字 = ''

    漢 = []
    羅 = []
    性=[]
    for (詞漢, 詞羅, 詞性) in 查教典詞性(漢字, 羅馬字):
        漢.append(詞漢)
        羅.append(詞羅)
        性.append(', '.join(詞性))
    return render(request, '文章/看文章.html', {
        '漢':漢,
        '羅':羅,
        '性':性,
    })


def 查教典詞性(漢字, 羅馬字):
    _詞性表 = {}
    with open('kiat4-ko2') as 檔案:
        for 漢, 羅, 詞性 in json.load(檔案):
            _詞性表[(漢, 羅)] = 詞性

    資料 = []
    for 詞物件 in(
        拆文分析器
        .對齊句物件(漢字, 羅馬字)
        .轉音(臺灣閩南語羅馬字拼音, '轉調符')
        .網出詞物件()
    ):
        詞漢 = 詞物件.看型()
        詞羅 = 詞物件.看音()
        try:
            詞性 = _詞性表[(詞漢, 詞羅)]
        except KeyError:
            詞性 = []
        資料.append((詞漢, 詞羅, 詞性))
    return 資料
