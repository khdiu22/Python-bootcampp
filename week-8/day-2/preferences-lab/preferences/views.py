from django.shortcuts import render, redirect

def home_view(request):
    theme = request.COOKIES.get('theme', 'light')
    cart = request.session.get('cart', [])
    return render(request, 'preferences/home.html', {
        'theme': theme,
        'cart': cart,
        'cart_count': len(cart),
    })

def set_theme_view(request):
    theme = request.GET.get('theme', 'light')
    if theme not in ['light', 'dark']:
        theme = 'light'
    response = redirect('home')
    response.set_cookie('theme', theme, max_age=30*24*60*60)
    return response

def add_to_cart_view(request):
    cart = request.session.get('cart', [])
    product_id = request.GET.get('product_id', '1')
    cart.append(product_id)
    request.session['cart'] = cart
    return redirect('home')

def clear_cart_view(request):
    request.session.pop('cart', None)
    return redirect('home')