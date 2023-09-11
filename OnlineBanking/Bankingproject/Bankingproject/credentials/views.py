from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import fill
from .form import fillform
# Create your views here.
def register(request):
    if request.method=='POST':
        Username=request.POST['Username']
        Password = request.POST['Password']
        Cpassword = request.POST['Password2']
        if Password == Cpassword:
            if User.objects.filter(username=Username).exists():
                messages.info(request, "username taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=Username,password=Password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'password not matching')
            return redirect('register')
            return redirect('/')
    return render(request, 'register.html')







def login(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        Password = request.POST['Password']
        user = auth.authenticate(username=Username, password=Password)
        if user is not None:
            auth.login(request, user)
            return redirect('new' )
        else:
            messages.info(request, "invalid credential")
            return redirect('login' )
    return render(request,'login.html')

def new(request):

    return render(request,'new.html')

def form1(request):
    end= messages.info(request, "invalid credential")



    return render(request,'form1.html',{'end':end})
def nn(request):
    return render(request,'nn.html')
def logout(request):
    auth.logout(request)
    return redirect('home')