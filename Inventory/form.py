from django import forms

from Inventory.models import Category, product,Order


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'

class ProductForm(forms.ModelForm):
     class Meta:
         model=product
         fields='__all__'


class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=('customer_name','customer_phone','customer_email','customer_address','product','qty')