from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from jsonfield.fields import JSONField


class 語料表(models.Model):
    原本漢字 = models.TextField()
    原本羅馬字 = models.TextField()
    漢字 = models.TextField()
    羅馬字 = models.TextField()
    詞性 = models.TextField(null=True, blank=True)

    備註 = models.TextField(blank=True)
    語料狀況 = models.ManyToManyField('語料狀況表', blank=True)

    標記者 = models.ForeignKey(
        User, null=True, related_name='+',  on_delete=models.CASCADE
    )
    標記時間 = models.DateTimeField(null=True)

    class Meta:
        verbose_name = "語料表"
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
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
        return '{} {}'.format(self.pk, self.顯示名())
