
from django.shortcuts import render, HttpResponse , redirect
from digishop.models import Product,ProductImages,User



def index(request):
    products = Product.objects.filter(active = True)
    print(products)
    data = {
        'products':products
    }
    return render(request,'index.html', data)

def logout(request):
    request.session.clear()
    return redirect('index')

def profile(request):

    return render(request,'profile.html')


