from django.shortcuts import render

# Create your views here.
def Portfolio(request):
    # d = {'profile_image_url': 'https://drive.google.com/uc?id=1VK0m5PgyBP-JytSnAB8_RGtHejrK1EoS',}
    return render(request,'Portfolio.html')