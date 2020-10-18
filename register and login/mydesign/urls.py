from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.conf.urls import url
from django.contrib import admin
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.index),
    url(r'^single/(\d+)/$', views.single),
    url(r'^comment/(\d+)/$', views.comment),
    url(r'^like/$', views.like),
    url(r'^movie/(\d+)/$', views.movie),
    url(r'^login/$', views.login),
    url(r'^register/$', views.register),
    url(r'^quit/$', views.quit),
    url(r'^person/$', views.person),
    url(r'^shuju/$',views.shuju),
    url(r'^shuju1/$',views.shuju1),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
