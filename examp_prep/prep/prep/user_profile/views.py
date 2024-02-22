from django.shortcuts import render

# Create your views here.
def index_profile(request):
    return render(request, 'user_profile/profile-details.html')