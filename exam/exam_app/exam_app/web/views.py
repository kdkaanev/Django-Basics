from django.shortcuts import render

from exam_app.user_profile.models import Profile







# Create your views here.
def base(request):
    profile = Profile.objects.first()

    context = {
        'profile': profile
    }
    return render(request, 'base.html', context)


def index(request):
    return render(request, 'web/index.html')
