from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from django.conf import settings
from 臺灣言語工具.翻譯.摩西工具.摩西用戶端 import 摩西用戶端
from 臺灣言語工具.翻譯.摩西工具.語句編碼器 import 語句編碼器


def 查國教院詞性(漢字, 羅馬字):
    句物件 = (
        拆文分析器
        .對齊句物件(漢字, 羅馬字)
        .轉音(臺灣閩南語羅馬字拼音)
    )
    try:
        return 物件查國教院詞性(句物件)
    except ConnectionRefusedError:
        空陣列 = [''] * len(句物件.網出詞物件())
        return 空陣列, 空陣列, ''


def 物件查國教院詞性(句物件):
    位址 = getattr(settings, 'TAI5TSUAN2HUA2', 'localhost')
    埠 = getattr(settings, 'TAI5TSUAN2HUA2PORT', '8080')
    用戶端 = 摩西用戶端(
        編碼器=語句編碼器,
        位址=位址, 埠=埠,
    )
    華語句物件, 臺語句物件, _分數 = 用戶端.翻譯分析(句物件)
    國教院詞性 = []
    國教院詞條 = []
    for 臺語詞 in 臺語句物件.網出詞物件():
        詞的可能詞性 = []
        詞條可能詞性 = []
        for 對應華語詞 in 臺語詞.翻譯目標詞陣列:
            字陣列 = 對應華語詞.篩出字物件()
            try:
                if 字陣列[-3].型 == '（' and 字陣列[-1].型 == '）':
                    # replace 愛提掉
                    詞的可能詞性.append(字陣列[-2].型.replace('VV2', 'V_2'))
                    詞條可能詞性.append(對應華語詞.看型().replace('VV2', 'V_2'))
            except IndexError:
                pass
        國教院詞性.append(', '.join(詞的可能詞性))
        國教院詞條.append(', '.join(詞條可能詞性))
    return 國教院詞性, 國教院詞條, 華語句物件.看型('', ' ')
