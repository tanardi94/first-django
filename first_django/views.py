from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title' : 'Home',
        'author' : 'Rahardian',
        'navigation' : [
            ['/', 'Home'],
            ['/blog/', 'Blog'],
            ['/about/', 'About'],
        ]
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')