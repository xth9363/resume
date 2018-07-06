from django.db import models


# Create your models here.

class Visitor(models.Model):
    class Meta:
        verbose_name = '访问者'
        verbose_name_plural = '访问者'

    ip = models.GenericIPAddressField(verbose_name='访问者Ip')
    visit_date = models.DateTimeField(auto_now_add=True, verbose_name='访问时间')

    def __str__(self):
        return "{}|{}".format(self.id, self.ip)
