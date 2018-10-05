from django import template
from 標記.models import 語料表
from math import ceil

register = template.Library()


@register.simple_tag
def 揀的最新一句():
    return _揀的最新一句()


@register.simple_tag
def 揀的頁數():
    return _揀的頁數()


@register.simple_tag
def 總共幾句():
    數量 = 語料表.objects.all().count()
    return 數量


def _揀的最新一句():
    try:
        編號 = 語料表.objects.exclude(
            揀的時間__isnull=True
        ).order_by(
            '-id'
        ).first().id
    except AttributeError:
        # 掠無編號
        編號 = 0
    return 編號


def _揀的頁數():
    編號 = _揀的最新一句()
    頁號 = ceil(編號 / 20)
    return 頁號
