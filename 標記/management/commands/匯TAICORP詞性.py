from django.core.management.base import BaseCommand
from django.db.transaction import atomic
from django.db.utils import IntegrityError


from 標記.models import 詞性表
from 標記.台灣閩南語詞類標記TAICORP import 詞性表 as TAICORP詞性表


class Command(BaseCommand):

    def handle(self, *args, **參數):
        print('詞性數量：{}'.format(詞性表.objects.count()), file=self.stdout)

        with atomic():
            for 詞, 華, 英 in zip(TAICORP詞性表[::3], TAICORP詞性表[1::3], TAICORP詞性表[2::3],):
                try:
                    詞性表.objects.create(
                        詞性=詞,
                        華文解釋=華,
                        英文解釋=英,
                    )
                except IntegrityError:
                    print('{} 可能匯過矣！'.format(詞), file=self.stdout)
                    raise
            詞性表.objects.create(
                詞性='PUNC',
                華文解釋='標點符號',
                英文解釋='Punctuation',
            )

        print('詞性數量：{}'.format(詞性表.objects.count()), file=self.stdout)
