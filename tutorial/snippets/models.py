from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# 得到所有lexers并从中筛选出本文件能用到的，item[1]代表lexers对应的语言
LEXERS = [item for item in get_all_lexers() if item[1]]
# 得到一个（语言名称，语言标识）的元组，item[0]代表lexers对应的语言的语言标识
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# 获取所有样式，并组成（样式名，样式名）的元组
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])
# 以上用于界面展示？

# Create your models here.
class Snippet(models.Model):
    created = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100, blank = True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']