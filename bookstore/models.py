from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField('书名', max_length=50, unique=True, default='')
    pub = models.CharField('出版社', max_length=100, default='')
    price = models.DecimalField('价格', max_digits=7, decimal_places=2)
    market_price = models.DecimalField('零售价', max_digits=7, decimal_places=2, default=0.0)
    info = models.CharField('描述', max_length=500, default='')
    is_active = models.BooleanField('是否活跃', default=True)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return f"{self.title}_{self.pub}_{self.price}_{self.market_price}"


class Author(models.Model):
    name = models.CharField('名字', max_length=11)
    age = models.IntegerField('年龄', default=1)
    email = models.EmailField('邮箱', null=True)

    class Meta:
        db_table = 'author'


class AuthorWife(models.Model):
    name = models.CharField('名字', max_length=11)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)

    class Meta:
        db_table = 'author_wife'
