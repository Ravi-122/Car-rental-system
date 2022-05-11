from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def Homepage(request):
    return render(request,'home.html')

def Login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Invalid User')
            return redirect('/login')

    else:
        return render(request,'login.html')

def aboutus(request):
    return render(request,'aboutus.html')

def register(request):
    if request.method == 'POST':
        first_name=request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        if(User.objects.filter(username=username).exists()):
            messages.info(request,"UserName Not Available")
            return redirect('/register')
        elif(User.objects.filter(username=username).exists()):
            messages.info(request,"Email Already Registered")
            return redirect('/register')
        else:
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password,
            )
            user.save()
            messages.info(request,"User Added")
            return redirect('/login')
    else:
        return render(request,'reg.html')

def Logout(request):
    auth.logout(request)
    return redirect('/')

def feedback(request):
    return render(request,'feedback.html')

def payment(request):
    return render(request,'payment.html')