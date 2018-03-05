import json

from django.core.management.base import BaseCommand
from 教典詞性.匯入教典 import 匯入教典內的詞性


class Command(BaseCommand):

    def handle(self, *args, **參數):
        with open('kiat4-ko2', 'w') as 檔案:
            json.dump(
                list(匯入教典內的詞性()), 檔案,
                ensure_ascii=False, indent=2,
            )
