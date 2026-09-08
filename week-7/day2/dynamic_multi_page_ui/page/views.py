from django.shortcuts import render


def home(request):
    context = {
        'page_title': 'Home',
        'welcome_message': 'Welcome to ShopEasy - your favorite online store',
    }
    return render(request, 'page/home.html', context)


def products(request):
    products_list = [
        {'name': 'laptop', 'price': 3500, 'stock': 5, 'category': 'Electronics'},
        {'name': 'coding book', 'price': 90, 'stock': 0, 'category': 'Books'},
        {'name': 'wireless headphones', 'price': 250, 'stock': 12, 'category': 'Electronics'},
        {'name': 'backpack', 'price': 120, 'stock': 8, 'category': 'Accessories'},
    ]

    # add ?empty=1 to the url to test the empty state
    if request.GET.get('empty') == '1':
        products_list = []

    context = {
        'page_title': 'Products',
        'products': products_list,
    }
    return render(request, 'page/products.html', context)


def about(request):
    context = {
        'page_title': 'About',
        'team_size': 4,
    }
    return render(request, 'page/about.html', context)
