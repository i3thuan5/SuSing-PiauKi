from http.client import HTTPSConnection
import json
import ssl

from django.core.management.base import BaseCommand
from django.db.transaction import atomic
from django.db.utils import IntegrityError


from 標記.models import 語料表


ssl.match_hostname = lambda _cert, _hostname: True


class Command(BaseCommand):
    su5lui7 = (
        'xn--kbr112a4oa73rtw5adwqr1d.xn--v0qr21b.xn--kpry57d'
    )
    tsu1liau7 = (
        '/%E5%8C%AF%E5%87%BA%E8%B3%87%E6%96%99%E5%BA%AB'
    )

    def handle(self, *args, **參數):
        print('語料表數量：{}'.format(語料表.objects.count()), file=self.stdout)

        c = HTTPSConnection(self.su5lui7)
        c.request("GET", self.tsu1liau7)
        資料 = json.loads(c.getresponse().read().decode())
        愛匯的資料 = []
        有出現的資料 = set()
        for 內容 in 資料['資料']:
            for 一句 in 內容['文章資料']:
                if '分詞' in 一句 and 一句['漢字'].strip():
                    這句 = (一句['漢字'], 一句['臺羅'])
                    if 這句 not in 有出現的資料:
                        愛匯的資料.append(這句)
                        有出現的資料.add(這句)
        with atomic():
            for 這句 in 愛匯的資料:
                漢, 羅 = 這句
                try:
                    語料表.objects.create(
                        原本漢字=漢, 原本羅馬字=羅
                    )
                except IntegrityError:
                    print(
                        '{} {} 可能匯過矣！'.format(一句['漢字'], 一句['臺羅']),
                        file=self.stdout
                    )
                    raise

        print('語料表數量：{}'.format(語料表.objects.count()), file=self.stdout)
