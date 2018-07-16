from django.db import models

# Create your models here.

class article(models.Model):
    """
    文章数据库表，标题，内容，创建时间和修改时间
    """
    title = models.CharField(default='',max_length=50,verbose_name='标题')
    content = models.TextField(default='',verbose_name='内容')
    ctime = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    mtime = models.DateTimeField(auto_now=True,verbose_name='修改时间')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
highlighted = models.TextField()