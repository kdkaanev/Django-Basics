from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from prep.album.models import Album
from prep.user_profile.models import Profile
from prep.web.views import get_profile


class DeleteProfileView(views.DeleteView):
    template_name = 'user_profile/profile-delete.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_profile()
# Create your views here.
class DetailsUserView(views.DetailView):
    template_name = 'user_profile/profile-details.html'

    def get_object(self, queryset=None):
        return get_profile()
