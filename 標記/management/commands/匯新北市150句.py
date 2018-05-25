import json
from urllib.request import urlopen

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    minnan900 = (
        'https://github.com/Taiwanese-Corpus/Sin1pak8tshi7_2015_900-le7ku3/'
        'raw/master/minnan900.json'
    )

    def handle(self, *args, **參數):
        with urlopen(self.minnan900) as 檔:
            資料 = json.loads(檔.read().decode())
        for _編號, 內容 in sorted(資料.items()):
            print(內容['例句漢字'], 內容['例句臺羅'])
