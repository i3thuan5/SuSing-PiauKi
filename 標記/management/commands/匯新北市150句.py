import json
from urllib.request import urlopen

from django.core.management.base import BaseCommand
from django.db.transaction import atomic
from django.db.utils import IntegrityError


from 標記.models import 語料表


class Command(BaseCommand):
    minnan900 = (
        'https://github.com/Taiwanese-Corpus/Sin1pak8tshi7_2015_900-le7ku3/'
        'raw/master/minnan900.json'
    )

    def handle(self, *args, **參數):
        print('語料表數量：{}'.format(語料表.objects.count()), file=self.stdout)

        with atomic():
            with urlopen(self.minnan900) as 檔:
                資料 = json.loads(檔.read().decode())
            for 編號, 內容 in sorted(資料.items()):
                if int(編號) <= 150:
                    try:
                        語料表.objects.create(
                            原本漢字=內容['例句漢字'], 原本羅馬字=內容['例句臺羅']
                        )
                    except IntegrityError:
                        print('可能匯過矣！', file=self.stdout)
                        raise

        print('語料表數量：{}'.format(語料表.objects.count()), file=self.stdout)
