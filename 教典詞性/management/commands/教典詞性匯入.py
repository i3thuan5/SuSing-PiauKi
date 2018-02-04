from django.core.management.base import BaseCommand
from 教典詞性.匯入教典 import 匯入教典內的詞性


class Command(BaseCommand):

    def handle(self, *args, **參數):
        匯入教典內的詞性()
