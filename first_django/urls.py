from django.conf.urls import url, include
from django.contrib import admin
from . import views
from blog import views as v_blog

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/$', include('about.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index)
]
