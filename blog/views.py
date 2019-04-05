#blog views
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title' : 'Blog',
        'author' : 'Rahardian',
        'navigation' : [
            ['/', 'Home'],
            ['/blog/', 'Blog'],
            ['/about/', 'About'],
        ]
    }
    return render(request,'blog/index.html',context)