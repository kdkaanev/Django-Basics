from django.urls import path

from prep.user_profile import views
from prep.user_profile.views import DetailsUserView

urlpatterns = (
    path('details/', DetailsUserView.as_view(), name='details'),
    path('delete/', views.DeleteProfileView.as_view(), name='delete'),
)