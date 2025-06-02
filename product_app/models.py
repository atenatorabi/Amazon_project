from django.db import models


# Create your models here.


class Product_color(models.Model):
    color = models.CharField(max_length=200 , verbose_name='رنگ')
    hex_code = models.CharField(max_length=200 , verbose_name='کد رنگی')
    def __str__(self):
        return self.color
    class Meta:
        verbose_name = 'رنگ'
        verbose_name_plural = 'رنگ ها'


class ProductCategory(models.Model):
    title = models.CharField(max_length=150, verbose_name="دسته")
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Product_List(models.Model):
    title = models.CharField(max_length=150, verbose_name="نام محصول")
    price = models.IntegerField(verbose_name='قیمت')
    is_active = models.BooleanField(default=True, verbose_name='موجود است')
    category = models.ForeignKey(ProductCategory , on_delete=models.CASCADE , null=True)
    color = models.ManyToManyField(to=Product_color)
    descroption = models.CharField(max_length=300, verbose_name='توضیحات')
    off = models.IntegerField(null=True, blank=True, verbose_name='تخفیف')
    count = models.IntegerField(verbose_name='تعداد موجودی')
    image = models.ImageField(upload_to='products/' , verbose_name='اضافه کردن عکس محصول' , null=True , blank=True)
    slug = models.SlugField(max_length=200 , allow_unicode=True , null=True , blank=True)
    def save(self,**kwargs):
        self.slug = self.title.replace(' ' , '-')
        return super(Product_List , self).save(**kwargs)

    def price_with_off(self):
        if self.off:
            return round(self.price - (self.price * (self.off / 100)))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
