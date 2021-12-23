from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from products.models import Product, ProductReal

def products_list(request: HttpRequest):
    product_list = Product.objects.order_by('-id')
    return render(request, 'products/product_list.html', {
        'product_list': product_list,
    })

def products_detail(request: HttpRequest, product_id):
    product_detail = get_object_or_404(Product, pk=product_id)
    product_reals = product_detail.product_reals.all()
    return render(request, 'products/product_detail.html', {
        'product_detail': product_detail,
        'product_reals': product_reals,
    })

def question_create(request: HttpRequest, product_id):
    return HttpResponse("안녕")