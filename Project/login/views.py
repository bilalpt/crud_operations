from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login ,logout as dj_logout





# Create your views here.


#Sign up
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def sighnup(request):
    if request.method=='POST':
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['email']
        pass1=request.POST['password1']
        pass2=request.POST['password2']

#Validation
        if fname.strip()==''or lname.strip()==''or email.strip()==''or pass1.strip()==''or pass2.strip()=='':
            messages.error(request,"Feild can't be blank")
            return redirect('sighnup')
        
        if pass1!=pass2:
            messages.error(request,"password dosen't Match")
            return redirect('sighnup')
        
        if User.objects.filter(username=fname).exists():
            messages.error(request, 'Username already exists')
            return redirect('sighnup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request,'Email already takon')
            return redirect('sighnup')
        
        user=User.objects.create_user(username=fname,last_name=lname,email=email,password=pass1)
        user.save()
        messages.success(request,'User crated successfully')
        return redirect(log)

    return render(request,'sighn.html')

#Login
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def log(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('dashbords')
        else:
            return redirect('home')
    if request.method =="POST":
        fname = request.POST['Name']
        pass1 = request.POST['Password']
        user =authenticate(username=fname,password=pass1)

# Validation
        if fname.strip() == '' or pass1.strip() == '':
            messages.error(request, "Fields can't be blank")
            return redirect('log')
        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return redirect('dashbords')
            else:
               return redirect('home')
        else:
            messages.error(request, "Your usename or password is Incorrect")
            return redirect('log')
    return render(request,'login.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='log')
def home(request):
    return render(request,'home.html')

# Logout
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='log')
def logout(request):
    dj_logout(request)
    return redirect('log')     
