from django.shortcuts import render

def index(request):
    context = {
        'title' : 'About',
        'author' : 'Rahardian',
        'navigation' : [
            ['/', 'Home'],
            ['/blog/', 'Blog'],
            ['/about/', 'About'],
        ]
    }
    return render(request,'index.html',context)
