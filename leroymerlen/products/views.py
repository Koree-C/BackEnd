from django.shortcuts import render

# Create your views here.


def products(request):
    context = {'title': 'Leroy Merlin',
               'products': [
                   {'image': '/static/assets/img/wardrobe.jpg',
                    'name': 'WOODEN WARDROBE',
                    'cost': 723.00}
               ]
    }
    return render(request, 'products/products.html', context)


def signup(request):
    return render(request, 'products/sign-up.html')
