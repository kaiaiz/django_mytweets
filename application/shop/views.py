from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse, render_to_response
from django.http import JsonResponse

from el_pagination.views import AjaxListView
from el_pagination.decorators import page_template
from rest_framework import viewsets

from .models import Category, Product

from cart.forms import CartAddProductForm


@page_template('product/products_list_page.html')
def product_list(request,
                 category_slug=None,
                 template='product/products_list.html',
                 extra_context=None):
    category = None
    categories = Category.objects.all()
    products_list = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products_list = products_list.filter(category=category)

    context = {'category': category,
               'categories': categories,
               'products_list': products_list}
    if extra_context is not None:
        context.update(extra_context)

    return render(request,
                  template,
                  context)


class ProductListView(AjaxListView):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)


    context_object_name = "products_list"
    template_name = "product/products_list.html"
    page_template = 'product/products_list_page.html'

    def get_queryset(self):
        return Product.objects.filter(available=True)

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    context = {'product': product,
               'cart_product_form': cart_product_form}

    return render(request,
                  'product/detail.html',
                  context)


def ajax_list(request):
    if request.method == 'POST':
        print request.POST['name']
        print request.POST['password']
        return HttpResponse('well done')
    else:
        return render(request, 'product/ajax_list.html')

