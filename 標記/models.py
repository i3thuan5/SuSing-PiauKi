from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class 語料表(models.Model):
    原本漢字 = models.TextField()
    原本羅馬字 = models.TextField()
    漢字 = models.TextField()
    羅馬字 = models.TextField()
    詞性 = models.TextField(blank=True)
    perplexity = models.FloatField(default=99999)
    來源 = models.TextField()

    備註 = models.TextField(blank=True)
    語料狀況 = models.ManyToManyField('語料狀況表', blank=True)

    先標記無 = models.BooleanField(default=False)
    標記者 = models.ForeignKey(
        User, null=True, related_name='+',  on_delete=models.CASCADE
    )
    標記時間 = models.DateTimeField(null=True)
    揀的時間 = models.DateTimeField(null=True)
    
    class Meta:
        verbose_name = "語料表"
        verbose_name_plural = verbose_name
        unique_together = ('原本漢字', '原本羅馬字',)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.漢字 = self.原本漢字
            self.羅馬字 = self.原本羅馬字
        super(語料表, self).save(*args, **kwargs)
        post_save.send(sender=self.__class__, instance=self)

    def __str__(self):
        return '{} {}'.format(self.id, self.漢字)

    def 狀況(self):
        陣列 = []
        for 狀況 in self.語料狀況.order_by('id'):
            陣列.append(str(狀況.id))
        return ', '.join(陣列)


class 語料狀況表(models.Model):
    狀況 = models.CharField(unique=True, max_length=30)
    確定會當用 = models.BooleanField(default=False)

    class Meta:
        verbose_name = "狀況表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{} {}'.format(self.pk, self.狀況)


class 詞性表(models.Model):
    詞性 = models.CharField(unique=True, max_length=30)
    華文解釋 = models.TextField(blank=True)
    英文解釋 = models.TextField(blank=True)
    備註 = models.TextField(blank=True)

    @classmethod
    def 全部(cls):
        return cls.objects.values_list('詞性', flat=True).order_by('詞性')
