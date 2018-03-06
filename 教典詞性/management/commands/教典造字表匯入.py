import json

from django.core.management.base import BaseCommand


from 教典詞性.編碼字 import 教典造字表資料


class Command(BaseCommand):

    def handle(self, *args, **參數):
        with open('tso3-ji7', 'w') as 檔案:
            json.dump(
                教典造字表資料.造字表(), 檔案,
                ensure_ascii=False, indent=2,
            )
