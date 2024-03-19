from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from Demo.models import*

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login



# Create your views here.
def index(request):
    indexdata=indexP.objects.all()
    data={
           'item': indexdata 
    }   
    return render(request,'index.html',data)

def about(request):
    aboutdata=aboutP.objects.all()
    data={
        'item':aboutdata 
    }
    return render(request,'about.html',data)

def cycle(request):
    cycledata=cycleP.objects.all()
    data={
        'item':cycledata
    }
    return render(request,'cycle.html',data)

def news(request):
    newsdata=newsP.objects.all() 
    data={
        'item':newsdata
    }
    return render(request,'news.html',data)

def contact(request):
     if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        number=request.POST['number']
        message=request.POST['massage']
        data=contactP.objects.create(Name=name,Email=email,Number=number,Message=message)
        data.save()
     return render(request,'contact.html')
 
def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        # phone= request.POST["phone"]
        data = User.objects.create_user(
            username, password=password, email=email, )
        data.save()
        return redirect('/login/')
    else:
        return render(request, "signup.html") 
    
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        print('user----', user)
        if user is not None: 
            login(request, user)
            return redirect('/home/')
        else:
            return HttpResponseRedirect('/login/')
    else:
        return render(request, "login.html")    