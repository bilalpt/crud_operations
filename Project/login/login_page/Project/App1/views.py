from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.
# def one_login(request):
#     if 'name' in request.session:
#         return redirect(home)
#     if request.method=='POST':
#         name=request.POST['Name']
#         password=request.POST['Password']
#         User=authenticate(name=name,password=password)
#         if User is not None:
#             request.session['name']=name
#             return redirect(home)
#         else:
#             print("invalid candidaate")
#     return render(request,'login.html')

# def home(request):
#     if 'name' in request.session:
#         return render(request,'home.html')
#     return redirect(one_login)

def bsp_login(request):
    if request.user.is_authenticated:
        return redirect(home2)
    if request.method=='POST':
        name=request.POST['Name']
        password=request.POST['Password']
        User=authenticate(name=name,password=password)
        if User is not None:
            login(request, User)
            return redirect(home2)
        else:
            print("invalid candidaate")
    return render(request,'bsp_login.html')

def home2(request):
    # if request.User.is_authenticated:
    return render(request,'home2.html')
    # return redirect(bsp_login)


