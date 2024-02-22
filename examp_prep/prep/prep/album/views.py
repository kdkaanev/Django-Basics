from django.shortcuts import render
from django.views import generic as views

from prep.album.models import Album
from prep.web.views import get_profile


class DetailAlbumView(views.DetailView):
    queryset = Album.objects.all()
    template_name = 'album/album-details.html'





# Create your views here.
class CreateAlbumView(views.CreateView):
    queryset = Album.objects.all()
    fields = ('album_name', 'artist', 'genre', 'description', 'image_url', 'price')
    template_name = 'album/album-add.html'

    success_url = '/'

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['album_name'].widget.attrs['placeholder'] = 'Album Name'
        form.fields['artist'].widget.attrs['placeholder'] = 'Artist'
        form.fields['description'].widget.attrs['placeholder'] = 'Description'
        form.fields['image_url'].widget.attrs['placeholder'] = 'Image URL'
        form.fields['price'].widget.attrs['placeholder'] = 'Price'

        return form

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = get_profile()
        return super().form_valid(form)








