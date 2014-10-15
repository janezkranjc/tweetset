from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import login as login_view
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from collect.models import Collection
from django.db.models import Count

from collect.forms import SignupForm

@login_required
def dashboard(request):
    collections = Collection.objects.filter(user=request.user).annotate(num_tweets=Count('tweets'))
    return render(request, 'collect/dashboard.html',
        {
            'collections':collections,
        })

def index(request):
    return render(request, 'collect/index.html')

@login_required
def account(request):
    return render(request, 'collect/index.html')

def collect_login(request, *args, **kwargs):
    if request.method == 'POST':
        if not request.POST.get('remember_me', None):
            request.session.set_expiry(0)
    return login_view(request, *args, **kwargs)

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            uname = form.data["email"]
            mail = uname
            passw = form.data["password"]
            new_user = User.objects.create_user(uname, mail, passw)
            user = authenticate(username=uname, password=passw)
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignupForm()

    return render(request, 'registration/signup.html', {
        'form':form
        })