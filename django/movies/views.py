from django.shortcuts import render

# Create your views here.
def home(request):
    movie = ['tennet', 'avatar', 'batman']
    context = {
        'movie' : movie,
    }
    return render(request,'movies/home.html',context)