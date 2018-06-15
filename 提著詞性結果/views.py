from http.client import HTTPSConnection
import json
import ssl
from urllib.parse import quote

from django.http.response import JsonResponse
from django.shortcuts import render


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 標記.models import 詞性表
from 提著詞性結果.國教院 import 查國教院詞性

# https://bugs.python.org/issue28414
# python 3.7已經修正
ssl.match_hostname = lambda cert, hostname: True


def 查詞性(request):
    漢字 = request.GET['漢字']
    羅馬字 = request.GET['羅馬字']

    return JsonResponse({'詞性': 查教典詞性(漢字, 羅馬字)})


def 查詞性頁(request):
    try:
        漢字 = request.GET['han']
        羅馬字 = request.GET['lo']
    except KeyError:
        漢字 = '「九月颱，無人知」，'
        羅馬字 = '“Káu-gue̍h-thai, bô lâng tsai”,'

    漢, 羅, 性 = 查教典詞性(漢字, 羅馬字)
    句物件 = (
        拆文分析器
        .對齊句物件(漢字, 羅馬字)
        .轉音(臺灣閩南語羅馬字拼音)
    )
    國教院詞性, 國教院詞條, 翻譯華語句 = 查國教院詞性(漢字, 羅馬字)
    程式詞性 = 物件查程式詞性(句物件)
    return render(request, '一句詞性/查一句.html', {
        'han': 漢字,
        'lo': 羅馬字,
        '漢': 漢,
        '羅': 羅,
        '性': 性,
        '國教院詞性': 國教院詞性,
        '國教院詞條': 國教院詞條,
        '國教院翻譯華語句': 翻譯華語句,
        '程式詞性': 程式詞性,
        '詞性種類': 詞性表.全部(),
        '預設詞性': 程式詞性,
    })


def 查教典詞性(漢字, 羅馬字):
    漢 = []
    羅 = []
    性 = []
    for (詞漢, 詞羅, 詞性) in _查教典詞性資料(漢字, 羅馬字):
        漢.append(詞漢)
        羅.append(詞羅)
        性.append(', '.join(詞性))
    return 漢, 羅, 性


def _查教典詞性資料(漢字, 羅馬字):
    _詞性表 = {}
    with open('kiat4-ko2') as 檔案:
        for 漢, 羅, 詞性 in json.load(檔案):
            _詞性表[(漢, 羅)] = 詞性
    with open('tso3-ji7') as 檔案:
        for 教典造字, unicode編碼字 in json.load(檔案).items():
            漢字 = 漢字.replace(教典造字, unicode編碼字)

    資料 = []
    原本句物件 = 拆文分析器.對齊句物件(漢字, 羅馬字)
    for 詞物件, 原本詞物件 in zip(
        原本句物件
        .轉音(臺灣閩南語羅馬字拼音, '轉調符')
        .網出詞物件(),
        原本句物件
        .網出詞物件(),

    ):
        詞漢 = 詞物件.看型()
        音陣列 = []
        for 字物件, 原本字物件 in zip(詞物件.篩出字物件(), 原本詞物件.篩出字物件()):
            if 原本字物件.敢有輕聲標記():
                音陣列.append('--' + 字物件.看音())
            else:
                音陣列.append(字物件.看音())
        詞羅 = '-'.join(音陣列).replace('---', '--')
        try:
            詞性 = _詞性表[(詞漢, 詞羅)]
        except KeyError:
            詞性 = []
        資料.append((詞漢, 詞羅, 詞性))
    return 資料


def 查程式詞性(漢字, 羅馬字):
    句物件 = (
        拆文分析器
        .對齊句物件(漢字, 羅馬字)
        .轉音(臺灣閩南語羅馬字拼音)
    )
    return 物件查程式詞性(句物件)


def 物件查程式詞性(句物件):
    conn = HTTPSConnection('xn--s-sng-vsa6h.xn--v0qr21b.xn--kpry57d')
    conn.request(
        "GET",
        '/{}'.format(
            quote(句物件.看分詞()),
        )
    )
    r1 = conn.getresponse()
    if r1.status != 200:
        print(r1.status, r1.reason)
        print(句物件.看分詞())
        raise RuntimeError()
    詞性結果 = []
    for _分詞, 詞性 in json.loads(r1.read().decode('utf-8')):
        詞性結果.append(詞性)
    return 詞性結果
