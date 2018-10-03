import csv

from django.core.management.base import BaseCommand


from 標記.models import 詞性表


class Command(BaseCommand):

    詞性 = set([
        'CONJ',
        'C',
        'MOD (< DEC, DEG) / EXT (< DER)',
        'ADV',
        'IJ',
        'LC',
        'NT',
        'DET',
        'QN',
        'DET',
        'NUM',
        'CL',
        'LC',
        'PN',
        'N',
        'P',
        'PRT',
        'COP',
        'EXIST',
        'VA',
        'V',
        'QP',
        'ASP',
        'ADJ',
        'FW',
        'HOO, KHI-HOO (予, 去予)',
        'Á (仔)',
        'WH',
        'NEG',
    ])

    def handle(self, *args, **參數):
        詞性表.objects.all().delete()

        tsong = set()
        with open('詞類比較.csv') as tong:
            for pit,資料 in enumerate(csv.reader(tong)):
                if pit == 0:
                    continue
                詞 = 資料[5].strip()
                if 詞:
                    tsong.add(詞)
        for 詞 in sorted(tsong):
            詞性表.objects.create(詞性=詞)

        print('詞性數量：{}'.format(詞性表.objects.count()), file=self.stdout)
