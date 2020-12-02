from django.db import models


# Create your models here.

class questions(models.Model):
    numbers = models.CharField(max_length=16, verbose_name='题目序号')
    content = models.TextField(verbose_name='内容')
    pic = models.CharField(max_length=100, verbose_name='图片')
    options = models.TextField(verbose_name='选项')
    answer = models.CharField(max_length=16, verbose_name='答案')
    option_number = models.CharField(max_length=16, verbose_name='选项数')
    reference = models.TextField(verbose_name='解释')

    def __str__(self):
        return self.numbers

    class Meta:
        db_table = 'question'


class Fraction(models.Model):
    name = models.CharField(max_length=16)
    fract = models.CharField(max_length=4)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Fraction'