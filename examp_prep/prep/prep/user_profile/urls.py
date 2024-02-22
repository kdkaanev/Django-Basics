from django.urls import path

from prep.user_profile import views

urlpatterns = (
    path('details/', views.index_profile, name='details'),
)