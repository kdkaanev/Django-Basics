import random

from django.shortcuts import render

# Create your views here.
def index(request):
    dogs = [
        'https://img.freepik.com/free-photo/cute-shepherd-dog-posing-isolated-white-background_155003-46179.jpg?size=626&ext=jpg',
        'https://img.freepik.com/premium-photo/golden-retriever-dog-sitting-floor-isolated_8595-251.jpg?size=626&ext=jpg'

    ]
    dog_name = [
        'Cute',
        'Golden',
    ]
    numbers = [i for i in range(-10,10)]
    context = {
        'dog_image': random.choice(dogs),
        'name': random.choice(dog_name),
        'numbers': numbers
    }
    return render(request, 'web/web-index.html',context)


def about(request):
    return render(request, 'web/about.html')

def show_bootstrap(request):
    context = {
        'has_bootstrap': request.GET.get('bootstrap')
    }
    return render(request, 'web/bootstrap.html', context)