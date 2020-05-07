from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Posts

# Create your views here.
def index(request):
    # return HttpResponse('Hello From Posts')

    posts = Posts.objects.all()[:10]
    context = {
        'title': 'Latest Posts',
        'posts': posts
    }

    return render(request, 'posts/index.html', context)

def details(request, id):
    post = Posts.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'posts/details.html', context)

@csrf_exempt 
def posts(request):
    if request.method == "POST":
        data = request.POST.copy()
        print("\nform request: ",request.POST.get("name"),"\n")
        return JsonResponse({"data": ["1",3,0]}, safe=False)
    
    return JsonResponse({"data": []}, safe=False)

def all_posts(request):
    posts = Posts.objects.all()[:10]
    result = [];

    for i in range(len(posts)):
        index = str(posts[i]).split(" ")[1]
        result.append({index: str(posts[i])})

    return JsonResponse(result, safe=False)

def about(request):
    return render(request, 'posts/about.html')
