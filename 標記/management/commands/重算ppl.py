import ssl

from django.core.management.base import BaseCommand
from django.db.transaction import atomic


from 標記.models import 語料表
from 臺灣言語工具.語言模型.KenLM語言模型 import KenLM語言模型
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


ssl.match_hostname = lambda _cert, _hostname: True


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'arpa',
            type=str,

        )

    def handle(self, *args, **參數):
        print('語料表數量：{}'.format(語料表.objects.count()), file=self.stdout)

        語言模型 = KenLM語言模型(參數['arpa'])
        with atomic():
            for 語料 in 語料表.objects.all():
                句物件 = 拆文分析器.對齊句物件(語料.漢字, 語料.羅馬字).轉音(臺灣閩南語羅馬字拼音)
                語料.perplexity = 語言模型.perplexity(句物件)
                語料.save()
