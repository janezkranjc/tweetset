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

from collect.utils import pagination_helper

from collect.forms import CollectionForm
from django.utils.text import slugify
import json
import gzip

@login_required
def download_json(request,collection_id):
    c = get_object_or_404(Collection,pk=collection_id,user=request.user)
    response = HttpResponse(content_type='application/gzip')
    response['Content-Disposition'] = 'attachment; filename="'+slugify(c.name)+'.json.gz"'
    list_of_tweets = []
    for t in c.tweets.all():
        list_of_tweets.append(t.data)
    with gzip.GzipFile(fileobj=response, mode="w") as f:
        f.write(json.dumps(list_of_tweets,indent=4))
    return response

@login_required
def tweets(request,collection_id):
    c = get_object_or_404(Collection,pk=collection_id,user=request.user)
    page = request.GET.get('page',1)
    tweets, show_first, show_last, page_numbers = pagination_helper(object_list=c.tweets.all(), page=page, per_page=25, allow_empty_first_page=True)
    return render(request, 'collect/tweets.html', {
        'collection':c,
        'tweets':tweets,
        'show_first':show_first,
        'show_last':show_last,
        'page_numbers':page_numbers,
        })

@login_required
def edit_collection(request,collection_id):
    c = get_object_or_404(Collection,pk=collection_id,user=request.user)
    if request.method == 'POST':
        form = CollectionForm(request.POST,instance=c)
        if form.is_valid():
            new_collection = form.save(commit=False)
            new_collection.save()
            return redirect('dashboard')
    else:
        form = CollectionForm(instance=c)
    return render(request, 'collect/edit_collection.html', {
        'collection':c,
        'form':form,
    })

@login_required
def new_collection(request):
    if request.method == 'POST':
        form = CollectionForm(request.POST)
        if form.is_valid():
            new_collection = form.save(commit=False)
            new_collection.user = request.user
            new_collection.save()
            return redirect('dashboard')
    else:
        form = CollectionForm()
    return render(request, 'collect/new_collection.html', {
        'form':form,
        })

@login_required
def stop_collection(request,collection_id):
    c = get_object_or_404(Collection,pk=collection_id,user=request.user)
    c.stop()
    return redirect('dashboard')

@login_required
def start_collection(request,collection_id):
    c = get_object_or_404(Collection,pk=collection_id,user=request.user)
    if c.start():
        messages.success(request,"Collection successfully started!")
    else:
        messages.error(request,"Collection could not be started.")
    return redirect('dashboard')

@login_required
def delete_collection(request,collection_id):
    c = get_object_or_404(Collection,pk=collection_id,user=request.user)
    c.delete()
    return redirect('dashboard')

@login_required
def dashboard(request):
    collections = Collection.objects.filter(user=request.user).annotate(num_tweets=Count('tweets'))
    return render(request, 'collect/dashboard.html',
        {
            'collections':collections,
        })

def index(request):
    return render(request, 'collect/index.html')

def collect_login(request, *args, **kwargs):
    return login_view(request, *args, **kwargs)
