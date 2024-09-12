from django.shortcuts import render

# Create your views here.
def webHomepage(request):
    return render(request, 'index.html')