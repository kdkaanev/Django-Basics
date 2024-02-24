from django.urls import path

from app.user_profile.views import ProfileCreateView, ProfileDetailsView

urlpatterns = (
    path('create/', ProfileCreateView.as_view(), name='create_profile'),
    path('details/', ProfileDetailsView.as_view(), name='profile_details'),
)