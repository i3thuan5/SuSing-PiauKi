import json

from django.http.response import JsonResponse
from django.shortcuts import render


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.翻譯.摩西工具.語句編碼器 import 語句編碼器
from 臺灣言語工具.翻譯.摩西工具.摩西用戶端 import 摩西用戶端
from 臺灣言語工具.基本物件.詞 import 詞


def 查詞性(request):
    漢字 = request.GET['漢字']
    羅馬字 = request.GET['羅馬字']

    return JsonResponse({'詞性': 查教典詞性(漢字, 羅馬字)})


def 查詞性頁(request):
    try:
        漢字 = request.GET['han']
        羅馬字 = request.GET['lo']
    except:
        漢字 = '「九月颱，無人知」，'
        羅馬字 = '“Káu-gue̍h-thai, bô lâng tsai”,'

    漢 = []
    羅 = []
    性 = []
    for (詞漢, 詞羅, 詞性) in 查教典詞性(漢字, 羅馬字):
        漢.append(詞漢)
        羅.append(詞羅)
        性.append(', '.join(詞性))

    國教院詞性, 國教院詞條, 翻譯華語句 = 查國教院詞性(漢字, 羅馬字)
    return render(request, '文章/看文章.html', {
        'han': 漢字,
        'lo': 羅馬字,
        '漢': 漢,
        '羅': 羅,
        '性': 性,
        '國教院詞性': 國教院詞性,
        '國教院詞條': 國教院詞條,
        '國教院翻譯華語句': 翻譯華語句,
    })


def 查教典詞性(漢字, 羅馬字):
    _詞性表 = {}
    with open('kiat4-ko2') as 檔案:
        for 漢, 羅, 詞性 in json.load(檔案):
            _詞性表[(漢, 羅)] = 詞性
    with open('tso3-ji7') as 檔案:
        for 教典造字, unicode編碼字 in json.load(檔案).items():
            漢字 = 漢字.replace(教典造字, unicode編碼字)

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


def 查國教院詞性(漢字, 羅馬字):
    用戶端 = 摩西用戶端(編碼器=語句編碼器, 位址='192.168.50.4')
    句物件 = (
        拆文分析器
        .對齊句物件(漢字, 羅馬字)
        .轉音(臺灣閩南語羅馬字拼音)
    )
    拆文分析器.分詞句物件('逐-家｜tak8-ke1 做-伙｜tso3-hue2 去｜khi3 食-飯｜tsiah8-png7 ！')
    華語句物件, 臺語句物件, _分數 = 用戶端.翻譯分析(句物件)
    國教院詞性 = []
    國教院詞條 = []
    for 臺語詞 in 臺語句物件.網出詞物件():
        詞的可能詞性 = set()
        詞條可能詞性 = []
        for 對應華語詞 in 臺語詞.翻譯目標詞陣列:
            字陣列 = 對應華語詞.篩出字物件()
            try:
                if 字陣列[-3].型 == '（' and 字陣列[-1].型 == '）':
                    詞的可能詞性.add(字陣列[-2].型)
                    詞條可能詞性.append(詞(字陣列[:-3]).看型())
            except IndexError:
                pass
        國教院詞性.append(', '.join(sorted(詞的可能詞性)))
        國教院詞條.append(', '.join(詞條可能詞性))
    return 國教院詞性, 國教院詞條, 華語句物件.看型('', ' ')
