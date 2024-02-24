from django.urls import path

from app.plant.views import index, CreatePlantView, CatalogueView, DetailsPlantView, EditPlantView, DeletePlantView

urlpatterns = (
    path('', index, name='home'),  # path()
    path('catalogue/',CatalogueView.as_view(), name='catalogue'),
    path('create/', CreatePlantView.as_view(), name='create_plant'),
    path('details/<int:pk>/', DetailsPlantView.as_view(), name='details_plant'),
    path('edit/<int:pk>/', EditPlantView.as_view(), name='edit_plant'),
    path('delete/<int:pk>/', DeletePlantView.as_view(), name='delete_plant'),
)