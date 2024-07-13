from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import DataB
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
    # feature1 = DataB()
    # feature1.id = 0
    # feature1.name = 'Fast'
    # feature1.details = "Our service is very quick"

    # feature2 = DataB()
    # feature2.id = 1
    # feature2.name = 'Fast'
    # feature2.details = "Our service is very quick"
    
    # features = [feature1, feature2]

    features = DataB.objects.all()
    context = {
        'name': 'Anthony',
        'age': 23,
        'school': 'University of Rwanda',
    }
    return render(request, 'index.html', {'feature': features, 'context': context})

def counter(request):
    words = request.POST['words']
    amount_of_words = len(words.split())
    return render(request, 'counter.html', {'data':words, 'amount_words':amount_of_words})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if  password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already Exist')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not the same')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Creadential invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')