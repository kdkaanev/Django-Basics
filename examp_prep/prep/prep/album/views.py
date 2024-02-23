from django.forms import modelform_factory
from django.urls import reverse_lazy
from django.views import generic as views

from prep.album.models import Album
from prep.web.views import get_profile


class MakePlaceholdersMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['album_name'].widget.attrs['placeholder'] = 'Album Name'
        form.fields['artist'].widget.attrs['placeholder'] = 'Artist'
        form.fields['description'].widget.attrs['placeholder'] = 'Description'
        form.fields['image_url'].widget.attrs['placeholder'] = 'Image URL'
        form.fields['price'].widget.attrs['placeholder'] = 'Price'

        return form
class MakeFieldsReadOnlyMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        for field in form.fields:
            form.fields[field].widget.attrs['readonly'] = 'readonly'


        return form



class DeleteAlbumView(MakeFieldsReadOnlyMixin,views.DeleteView):


    queryset = Album.objects.all()
    form_class = modelform_factory(Album, fields=('album_name', 'artist', 'genre', 'description', 'image_url', 'price'))
    template_name = 'album/album-delete.html'
    success_url = reverse_lazy('index')




    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()
        return kwargs






class EditAlbumView(MakePlaceholdersMixin,views.UpdateView):
    queryset = Album.objects.all()
    fields = ('album_name', 'artist', 'genre', 'description', 'image_url', 'price')
    template_name = 'album/album-edit.html'
    success_url = reverse_lazy('index')


class DetailAlbumView(views.DetailView):
    queryset = Album.objects.all()
    template_name = 'album/album-details.html'


# Create your views here.
class CreateAlbumView(MakePlaceholdersMixin,views.CreateView):
    queryset = Album.objects.all()
    fields = ('album_name', 'artist', 'genre', 'description', 'image_url', 'price')
    template_name = 'album/album-add.html'

    success_url = reverse_lazy('index')



    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = get_profile()
        return super().form_valid(form)
