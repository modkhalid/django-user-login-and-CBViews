from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.generic import View,TemplateView,ListView,DetailView
from . import models
class CBView(View):
     def get(self,request):
         return HttpResponse("hi this is test")


class templateView(TemplateView):
    template_name="myapp/index.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)

        context['title']="khalid"
        return context

class SchoolListView(ListView):
    context_object_name="schools"
    model=models.School #Now it will serach for myview/school_list(models Name).html in temmplate
    # template_name='myview/school_list.html'

class SchoolDetailView(DetailView):
    context_object_name="school_detail"
    model=models.School
    template_name='myview/school_detail.html'
