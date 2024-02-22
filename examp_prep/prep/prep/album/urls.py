from django.urls import path

from prep.album.views import CreateAlbumView, DetailAlbumView





urlpatterns = (
    path('add/', CreateAlbumView.as_view(), name='create-album'),
    path('<int:pk>/details/', DetailAlbumView.as_view(), name='detail-album'),
)