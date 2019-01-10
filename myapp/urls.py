from django.conf.urls import url
from myapp import views
app_name='my_app'
urlpatterns=[

    url(r'^home/$',views.home,name="home"),
    url(r'^register/$',views.register,name="register"),
    url(r'^login/',views.login_user,name="login")
]
