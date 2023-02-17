from django.shortcuts import render

# Create your views here.
def app_dirs(request):
    return render(request, 'demo/readme.html')

def dirs(request):
    return render(request, 'dirs.html')