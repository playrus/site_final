from django.db import models
from products.models import Product
from django.db.models.signals import post_save

class Status(models.Model):
    name=models.CharField(max_length=24)
    is_active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)

    def __str__(self):
        return "Статуc %s" % self.name

    class Meta:
        verbose_name = 'Статус заказы'
        verbose_name_plural = 'Статусы заказа'

class Order(models.Model):
    total_price = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    customer_name=models.CharField(max_length=128)
    customer_email=models.EmailField()
    customer_phone=models.CharField(max_length=11)
    customer_address=models.CharField(max_length=128,blank=False,null=True,default=None)
    comments = models.TextField(blank=True,null=True,default=None)
    status=models.ForeignKey(Status,on_delete=models.CASCADE, blank=True,null=True,default=None)
    created=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    def __str__(self):
        return "Заказ %s %s" % (self.id, self.status.name)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class ProductInOrder(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE, blank=True,null=True,default=None)
    product = models.ForeignKey(Product,on_delete=models.CASCADE, blank=True,null=True,default=None)
    number = models.IntegerField(default=1)
    price_per_item=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    total_price = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    is_active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)
    
    def __str__(self):
        return "%s" % self.product.name

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'
    
    def save(self, *args, **kwargs):
        self.price_per_item = self.product.price
        self.total_price=self.number * self.price_per_item
       
        super(ProductInOrder.save(*args,**kwargs))

def product_in_order_post_save(sender,instance,created,**kwargs):
    order = instance.order
    all_products_in_order=ProductInOrder.objects.filters(order=order,is_active=True)
    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price
    instance.order_total_price = order_total_price
    instance.order.save(force_update=True)

post_save.connect(product_in_order_post_save, sender=ProductInOrder)