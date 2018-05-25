
from django.core.management.base import BaseCommand
from django.db.transaction import atomic
from django.db.utils import IntegrityError


from 標記.models import 語料狀況表


class Command(BaseCommand):

    def handle(self, *args, **參數):
        print('狀況數量：{}'.format(語料狀況表.objects.count()), file=self.stdout)

        with atomic():
            for 狀況 in [
                "範例",
                "愛討論",
                "斷詞有問題",
            ]:
                try:
                    語料狀況表.objects.create(狀況=狀況)
                except IntegrityError:
                    print('{} 可能匯過矣！'.format(狀況), file=self.stdout)
                    raise

        print('狀況數量：{}'.format(語料狀況表.objects.count()), file=self.stdout)
