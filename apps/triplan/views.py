from django.shortcuts import render, redirect, HttpResponse
from django.contrib import admin, messages

from .models import User, Triplan, Favlist


# Create your views here.

def mytrips(request):
    print request.session['id']
    user = User.userManager.get(id=request.session['id'])
    context = {
    "trip": Triplan.triplanManager.exclude(user=user),
    "person": user,
    "mytrips": Triplan.triplanManager.filter(user=user),
    "alltrips": Favlist.objects.filter(user=user)
    }
    return render(request, 'yourtriptresults.html', context)

def addtrip(request, id):
        if request.method == 'POST':
        #user.UserManager.registration, the registration part is the function itself that you defined within the method.
            trip_tuple = Triplan.triplanManager.addrip(request.POST['destination'],request.POST['description'],request.session['id'],
            request.POST['travel_from'], request.POST['travel_to'])

            if trip_tuple[0] == True:
                request.session['id'] = trip_tuple[1]
                user = User.userManager.filter(id=request.session['id'])
                return redirect('/triplan/mytrips')

            else:
                for key,error in trip_tuple[1].iteritems():
                    messages.error(request, error)
                    return render(request, 'addplan.html')

def addtripload(request):
    return render(request, 'addplan.html')

def others(request, id):
    trip = Triplan.triplanManager.get(id=id)
    content = {
        'trip':trip,
        'others':Favlist.objects.filter(triplan=trip)
    }
    return render(request, 'others.html', content)

def join(request, id):
    trip = Triplan.triplanManager.get(id=id)
    user = User.userManager.get(id=request.session['id'])
    Favlist.objects.create(user=user, triplan=trip)
    return redirect('/triplan/mytrips')
