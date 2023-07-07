from _decimal import Decimal
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView, UpdateView,View,DetailView

from Inventory.models import Category, product,Order
from Inventory import form


# Create your views here.

class HomeView ( TemplateView ):
    template_name = 'index.html'

    # def ger_context_data(self,**kwargs):


class AddCategoryView ( CreateView ):
    form_class = form.CategoryForm
    template_name = 'add_category.html'
    queryset = Category.objects.all ( )
    success_url = '/category/'


class CategoryListView ( ListView ):
    template_name = 'CategoryListView.html'
    queryset = Category.objects.all ( )
    context_object_name = 'objects'

class CategoryEditView(UpdateView):
    form_class = form.CategoryForm
    template_name = 'edit_category.html'
    queryset = Category.objects.all ( )
    success_url = '/category/'
    pk_url_kwarg='pk'


# class CategoryEditView(View):
#     def get(self,request,pk):
#         instance=Category.objects.get(pk=pk)
#         context={
#             'category_id':pk,
#             'form':form.CategoryForm(instance=instance)
#         }
#         return render(request,template_name='edit_category.html',context=context )
#
#     def post(self,request,pk):
#         instance = Category.objects.get ( pk=pk )
#         forms=form.CategoryForm(instance=instance,data=request.POST)
#         if forms.is_valid():
#             forms.save()
#         context = {
#             'category_id': pk,
#             'form': form.CategoryForm ( instance=instance )
#         }
#         return render ( request, template_name='edit_category.html', context=context )
class DeleteView(View):

    def get(self,request,pk):
        instance = Category.objects.get ( pk=pk )
        instance.delete()
        return redirect('/category/')

class ProductListView ( ListView ):
        template_name = 'ProductList.html'
        queryset = product.objects.all ( )
        context_object_name = 'objects'


class AddProductView ( CreateView ):
    form_class = form.ProductForm
    template_name = 'add-product.html'
    queryset = product.objects.all ( )
    success_url = '/product/'

class CreateOrderView ( View ):

        form_class = form.ProductForm
        template_name = 'add-product.html'
        queryset = product.objects.all ( )
        success_url = '/product/'

        def get(self,request):
            context={
                'form':form.OrderForm
            }

            return render(request,'add_Order.html',context=context)

        def post(self,request):
            forms=form.OrderForm(request.POST)
            if forms.is_valid():
                customer_name=forms.data['customer_name']
                customer_phone = forms.data['customer_phone']
                customer_email = forms.data['customer_email']
                customer_address = forms.data['customer_address']
                product_id=forms.data['product']
                products=product.objects.get(id=product_id)
                qty=forms.data['qty']
                subtotal=Decimal(products.price)*Decimal(qty)
                vat=Decimal(subtotal/100)*Decimal(15)
                total=subtotal+vat

                order=Order.objects.create(
                    product=products,qty=qty,subtotal=subtotal,vat=vat,total=total,customer_name=customer_name,
                    customer_phone=customer_phone,customer_email=customer_email,customer_address=customer_address
                )
                order.save()
            context={
                 'form':form.OrderForm
             }
            return render(request,'add_Order.html',context=context)


class OrderListView ( ListView ):
    template_name = 'orderList.html'
    queryset = Order.objects.all ( )
    context_object_name = 'objects'

class OrderDitailsView(DetailView):
    template_name = 'invoice.html'
    queryset = Order.objects.all ( )
    context_object_name = 'object'