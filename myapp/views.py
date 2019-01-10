from django.shortcuts import render
from myapp.forms import UserBasicForm,UserProfileForm
# Create your views here.

from django.contrib.auth import login,logout,authenticate
from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'myapp/index.html',{'title':"index-page"})

def home(request):
    return render(request,'myapp/home.html',{'title':"home-page"})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    # return render(request,'myapp/register.html',{'title':"register-page"})
    registered=False
    if request.method=='POST':
        user_form=UserBasicForm(request.POST)
        profile_form=UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save(commit=True)
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
            profile.save()
            registered=True


        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserBasicForm()
        profile_form=UserProfileForm()

    return render(request,'myapp/register.html',{'registered':registered,'user_form':user_form,'profile_form':profile_form})



def login_user(request):
    # return render(request,'myapp/login.html',{'title':"Login-page"})
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        # getauthenticate
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('USER IS NOT ACTIVE ')
            # return HttpResponseRedirect(reverse('index'))
        else:
            print('User tried {} and password {}'.format(username,password))
    else:
        return render(request,'myapp/login.html',{'title':"Login-page"})
