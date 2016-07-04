from django.shortcuts import render, redirect, HttpResponse
from django.contrib import admin, messages

from .models import User

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        user_tuple_login = User.userManager.login(request.POST['user_name'], request.POST['user_password'])
        print user_tuple_login[0]
        if user_tuple_login[0] == True:
            print user_tuple_login[0]
            request.session['id'] = user_tuple_login[1].id
            return redirect('/registering')

        else:
            errors = user_tuple_login[1]
            for key,error in user_tuple_login[1].iteritems():
                messages.error(request, error)
            return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
    #user.UserManager.registration, the registration part is the function itself that you defined within the method.
        user_tuple = User.userManager.register(request.POST['first_name'],request.POST['last_name'],
        request.POST['user_name'], request.POST['user_password'], request.POST['user_confirm_password'])

        if user_tuple[0] == True:
            request.session['id'] = user_tuple[1].id
            return redirect('/registering')

        else:
            for key,error in user_tuple[1].iteritems():
                messages.error(request, error)
                return render(request, 'index.html')

def registering(self):
    return redirect('/triplan/mytrips')
