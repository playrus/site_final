from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=128)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'

class Product(models.Model):
    name=models.CharField(max_length=128)
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    description = models.TextField(blank=True,null=True,default=None)
    is_active=models.BooleanField(default=True)
    discount = models.IntegerField(default=0)
    is_discount=models.BooleanField(default=False)
    category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE, blank=True,null=True,default=None)
    created=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE, blank=True,null=True,default=None)
    is_main = models.BooleanField(default=False)
    image = models.ImageField(upload_to='products_images/')
    created=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'