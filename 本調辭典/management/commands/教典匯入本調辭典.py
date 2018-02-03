from django.core.management.base import BaseCommand
from 本調辭典.匯入教典 import 匯入教典內的詞


class Command(BaseCommand):

    def handle(self, *args, **參數):
        匯入教典內的詞()
