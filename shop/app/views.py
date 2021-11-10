from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login as user_login, logout
from django.template import RequestContext
from .forms import *
from .models import *
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib import messages


def index(request):
    return render(request, 'base.html')


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    page = request.GET.get('page')

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    paginator = Paginator(products, 9)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'page': page,
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
            messages.success(request, 'Вы успешно зарегестрировались!')
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


def product(request, product_id):
    product = Product.objects.get(id=product_id)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    return render(request, 'detail.html', locals())



def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print(request.POST)
    data = request.POST
    product_id = data.get("product_id")
    nmb = data.get("nmb")
    is_delete = data.get("is_delete")

    if is_delete == 'true':
         product = ProductInBasket.objects.filter(id=product_id).update(is_active=False)
    else:
        new_product, created = ProductInBasket.objects.get_or_create(
            session_key=session_key,
            product_id=product_id,
            is_active=True,
            defaults={"nmb": nmb})

        if not created:
            new_product.nmb += int(nmb)
            new_product.save(force_update=True)

    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    products_total_nmb = products_in_basket.count()

    return_dict["products_total_nmb"] = products_total_nmb
    return_dict["products"] = products_total_nmb

    return_dict["products"] = list()

    for item in products_in_basket:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["name"] = item.product.name
        product_dict["price_per_item"] = item.price_per_item
        product_dict["nmb"] = item.nmb
        return_dict["products"].append(product_dict)

    return JsonResponse(return_dict)


def checkout(request):
    session_key = request.session.session_key
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    print (products_in_basket)
    for item in products_in_basket:
        print(item.order)


    form = CheckoutContactForm(request.POST or None)
    if request.POST:
        print(request.POST)
        if form.is_valid():
            print("yes")
            data = request.POST
            name = data.get("name", "3423453")
            phone = data["phone"]
            user, created = User.objects.get_or_create(username=phone, defaults={"first_name": name})

            order = Order.objects.create(user=user, customer_name=name, customer_phone=phone, status_id=1)

            for name, value in data.items():
                if name.startswith("product_in_basket_"):
                    product_in_basket_id = name.split("product_in_basket_")[1]
                    product_in_basket = ProductInBasket.objects.get(id=product_in_basket_id)
                    print(product_in_basket)
                    print(type(value))

                    product_in_basket.nmb = value
                    product_in_basket.order = order
                    product_in_basket.save(force_update=True)

                    ProductInOrder.objects.create(product=product_in_basket.product, nmb=product_in_basket.nmb,
                                                  price_per_item=product_in_basket.price_per_item,
                                                  total_price=product_in_basket.total_price,
                                                  order=order)

            return redirect('/')
        else:
            print("no")
    return render(request, 'shop/checkout.html', locals())


def profile_edit(request):
    if request.method == 'GET':
        try:
            current_profile = Profile.objects.get(pk=request.user.id)
        except (AttributeError, Profile.DoesNotExist):
            current_profile = None
        if not request.user.is_authenticated:
            return redirect('/auth/login')
        current_profile.first_name = request.user.first_name
        current_profile.last_name = request.user.last_name
        current_profile.user.email = request.user.email
        profile_form = ProfileForm(instance=current_profile)
    else:
        current_profile = Profile.objects.get(pk=request.user.id)
        current_profile.phone = request.POST.get('phone')
        current_profile.city = request.POST.get('city')
        current_profile.avatar = request.FILES.get('avatar')
        current_profile.save()
        profile_form = ProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile_form.save()
        messages.success(request, "Вы успешно изменили ваш профиль!")
        if profile_form:
            return redirect('/profile_edit')

    return render(request, 'shop/profile_edit.html', {
        'form': profile_form,
        'first_name': current_profile.first_name,
        'last_name': current_profile.last_name,
        'email': current_profile.user.email
    })



