from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.checks import messages
from django.shortcuts import render, redirect
from .models import Languages_offered,Contact_us,Langs,Teachers,user_Registration


def home(request):
    lo = Languages_offered.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        print(name)
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact_us(name=name, email=email, phone=phone, message=message)
        contact.save()
    return render(request, 'index.html', {'result': lo})
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        print(name)
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact_us(name=name, email=email, phone=phone, message=message)
        contact.save()
        return redirect("/index")
    return render(request,'contact.html')
def shop(request):
    return render(request,'shop.html')
def loginasuser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request,'afterlogin.html')

    return render(request,'loginasuser.html')
def loginastutor(request):
    return render(request,'loginastutor.html')
def signupasuser(request):
    if request.method=='POST':
        first_name= request.POST['first_name']
        username = request.POST['username']
        password = request.POST['password']
        user= User.objects.create_user(first_name=first_name,username=username,password=password)
        user.save();
        return redirect('/userpage')
    return render(request,'signupasuser.html')
def signupastutor(request):
    if request.method=='POST':
        first_name= request.POST['first_name']
        username = request.POST['username']
        user= User.objects.create_user(first_name=first_name,username=username)
        user.save();
        return redirect('/userpage')
    return render(request,'signupastutor.html')
def userpage(request):
        if request.method == 'POST':
            name= request.POST.get('name')
            lang= request.POST.get('lang')
            email= request.POST.get('email')
            phone= request.POST.get('phone')
            password= request.POST.get('password')
            password1= request.POST.get('password1')
            if password==password1:
                registration = user_Registration(name=name, lang=lang, email=email, phone=phone,password=password)
                registration.save();
                print("User Created")
                return redirect('/afterlogin')
            else:
                print("Passsword Not matching, Try again")
        return render(request,'userpage.html')
def afterlogin(request):
    return render(request,'afterlogin.html')
def languages(request):
    langs = Langs.objects.all()
    return render(request,'languages.html',{'res':langs})
def teachers(request):
    teacher=Teachers.objects.all()
    return render(request,'teachers.html',{'res1':teacher})
def choiceofteacher(request):
    return render(request,'choiceofteacher.html')

