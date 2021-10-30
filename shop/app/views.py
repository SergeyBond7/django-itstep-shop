from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from django.contrib.auth import login as user_login, logout
from .forms import *
from .models import Profile



def index(request):
    return render(request, 'base.html')


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product})


def about(request):
    return render(request, 'shop/about.html')


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            user_login(request, user)
            return redirect('/')
        else:
            pass
    else:
        form = UserLoginForm()
    return render(request, 'shop/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return redirect('/login')
        else:
            pass
    else:
        form = UserRegisterForm()
    return render(request, 'shop/register.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('/login')