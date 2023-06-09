from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id_
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.

def store(request, category_slug=None ):
    categories = None
    products = None
    
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.all().filter(category=categories, is_available=True)
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter().order_by('id')
        #filterin içine is_available=True yapıyoruz.
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
     
    context={
        'products': paged_products,
        'product_count': product_count,
    }
     
    return render(request,'store/store.html', context)

def product_detail(request,category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id = _cart_id_(request), product=single_product).exists()
     
    except Exception as e:
        raise e
    
    context = {
        'single_product': single_product,
        'in_cart': in_cart,
    }
    return render(request,'store/product_detail.html', context)

def search(request):
    products=None
    if 'keyword' in request.GET:
        keyword = request.GET.get('keyword')
        if keyword:
    #         products = Product.objects.order_by('-created_date').filter(description__icontains=keyword) \
    # | Product.objects.filter(title__icontains=keyword)
    
        #     products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword)) \
        # | Product.objects.filter(Q(title__icontains=keyword)) | Product.objects.filter(author__icontains=keyword) \
        # | Product.objects.filter(Q(category__icontains=keyword))
            products = Product.objects.filter(
                Q(description__icontains=keyword) |
                Q(title__icontains=keyword) |
                Q(author__icontains=keyword) |  
                Q(publisher__icontains=keyword) |
                Q(language__icontains=keyword) |
                Q(barcode__icontains=keyword) 
            ).order_by('-created_date')
            product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
    }
       
    return render(request,'store/store.html', context)
    
  