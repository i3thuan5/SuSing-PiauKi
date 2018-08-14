from django import template
from 標記.models import 語料表

register = template.Library()


@register.simple_tag
def 揀的最新一句():
    return _揀的最新一句()


@register.simple_tag
def 總共幾句():
    數量 = 語料表.objects.all().count()
    return 數量


def _揀的最新一句():
    編號 = 語料表.objects.filter(先標記無=True).order_by('揀的時間','-id')[0]
    return 編號 


def 揀的最新一句佇to一頁():
    編號 = 語料表.objects.filter(先標記無=True).latest('揀的時間').id
    頁號 = 編號 / 20
    return 頁號
