from django import forms
from django.shortcuts import render, redirect
from django.views.generic import View as views, CreateView

from prep.album.models import Album
from prep.user_profile.models import Profile
from prep.web.forms import CreateProfileForm


# Create your views here.





def get_profile():
    return Profile.objects.first()
def get_albums():
    return Album.objects.all()





def create_profile(request):
    form = CreateProfileForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'web/home-no-profile.html', context)




def index(request):
    profile = get_profile()
    context = {

        'albums': get_albums()
    }

    if not profile:
        return create_profile(request)
    return render(request, 'web/home-with-profile.html', context)
