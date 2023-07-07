import uuid

from django.db import models

from Inventory.constant import stockStatus


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField(blank=True,null=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    qty=models.IntegerField(default=0)
    price=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    stock_status=models.SmallIntegerField(choices=stockStatus.choices,default=stockStatus.IN_STOCK)

    def __str__(self):
        return self.name

class Order(models.Model):
        invoice_no=models.CharField(max_length=100,unique=True,default=uuid.uuid4)
        product=models.ForeignKey(product,on_delete=models.CASCADE)
        qty=models.IntegerField(default=1)
        price = models.DecimalField ( max_digits=10, decimal_places=2, default=0.00 )
        subtotal = models.DecimalField ( max_digits=10, decimal_places=2, default=0.00,editable=False )
        vat = models.DecimalField ( max_digits=10, decimal_places=2, default=0.00,editable=False )
        total = models.DecimalField ( max_digits=10, decimal_places=2, default=0.00,editable=False  )
        customer_name=models.CharField(max_length=100,null=True,blank=True)
        customer_phone = models.CharField ( max_length=100, null=True, blank=True )
        customer_email = models.CharField ( max_length=100, null=True, blank=True )
        customer_address = models.CharField ( max_length=100, null=True, blank=True )

        def __str__(self):
            return self.invoice_no
