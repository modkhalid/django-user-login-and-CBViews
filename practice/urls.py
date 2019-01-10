from django.conf.urls import url,include
from django.contrib import admin
from myapp import views

urlpatterns = [
    url(r'^logout/$',views.logout_user,name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index,name="index"),
    url(r'^myapp/$',views.home,name="home"),
    url(r'^myapp/',include('myapp.urls')),
    url(r'^myview/',include('myview.urls'))
]
