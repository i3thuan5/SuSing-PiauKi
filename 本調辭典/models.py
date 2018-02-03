from django.db import models
from 臺灣言語工具.辭典.型音辭典 import 型音辭典
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


class 本調辭典表(models.Model):
    分詞 = models.CharField(
        max_length=100,
        unique=True,
    )

    @classmethod
    def 全部分詞(cls):
        return set(cls.objects.all().values_list('分詞', flat=True))

    @classmethod
    def 辭典物件(cls):
        本調辭典 = 型音辭典(4)
        for 分詞 in cls.全部分詞():
            本調辭典.加詞(
                拆文分析器.分詞詞物件(分詞)
            )
        return 本調辭典
