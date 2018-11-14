from django.core.exceptions import SuspiciousOperation
from django.test.testcases import TestCase
from 標記.管理.基礎句選擇 import 基礎句選擇表


class 句接做伙試驗(TestCase):
    def setUp(self):
        self.it = 基礎句選擇表.objects.create(
            原本漢字='因為今仔日落雨，',
            原本羅馬字='In-uī kin-á-ji̍t lo̍h-hōo,',
        )
        self.ji = 基礎句選擇表.objects.create(
            原本漢字='我就想講：',
            原本羅馬字='Guá tsiū siūnn-kóng:',
        )
        self.sam = 基礎句選擇表.objects.create(
            原本漢字='莫出門好矣',
            原本羅馬字='mai2 tshut-mn̂g hó--ah',
        )
        self.tsuan = 基礎句選擇表.objects.filter(
            pk__in=[self.it.pk, self.ji.pk, self.sam.pk]
        )

    def test_羅數量是著的(self):
        基礎句選擇表.kap(self.tsuan)
        self.assertEqual(
            len(基礎句選擇表.objects.get(pk=self.it.pk)),
            18
        )

    def test_頭一句的原本內容是三句原本內容接做伙(self):
        基礎句選擇表.kap(self.tsuan)
        self.assertEqual(
            基礎句選擇表.objects.get(pk=self.it.pk).原本羅馬字,
            (
                'In-uī kin-á-ji̍t lo̍h-hōo, '
                'Guá tsiū siūnn-kóng: '
                'mai2 tshut-mn̂g hó--ah'
            )
        )

    def test_頭一句有揀(self):
        self.tsuan.update(先標記無=False)
        基礎句選擇表.kap(self.tsuan)
        self.assertTrue(
            基礎句選擇表.objects.get(pk=self.it.pk).先標記無
        )

    def test_後壁的句無揀(self):
        self.tsuan.update(先標記無=True)
        基礎句選擇表.kap(self.tsuan)
        self.assertFalse(
            基礎句選擇表.objects.get(pk=self.ji.pk).先標記無
        )
        self.assertFalse(
            基礎句選擇表.objects.get(pk=self.sam.pk).先標記無
        )

    def test_愛連號才有通接(self):
        with self.assertRaises(SuspiciousOperation):
            基礎句選擇表.kap(
                基礎句選擇表.objects.filter(
                    pk__in=[self.it.pk, self.sam.pk]
                )
            )
