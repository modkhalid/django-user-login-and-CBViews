from django.conf.urls import url
from myview import views
app_name='my_view'
urlpatterns=[
    url(r'^$',views.CBView.as_view(),name="home"),
    url(r'^view/$',views.templateView.as_view(),name="viewTempa"),
    url(r'^list/$',views.SchoolListView.as_view(),name="list"),
    url(r'^list/(?P<pk>[0-9]+)/$',views.SchoolDetailView.as_view(),name="detail"),
]
