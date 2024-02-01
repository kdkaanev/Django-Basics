import random

from django.shortcuts import render

# Create your views here.
def index(request):
    dogs = [
        'https://img.freepik.com/free-photo/cute-shepherd-dog-posing-isolated-white-background_155003-46179.jpg?size=626&ext=jpg',
        'https://img.freepik.com/premium-photo/golden-retriever-dog-sitting-floor-isolated_8595-251.jpg?size=626&ext=jpg'

    ]
    context = {
        'dog_image': random.choice(dogs),
    }
    return render(request, 'web/web-index.html',context)