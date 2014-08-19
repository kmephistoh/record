from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import * 

# Create your views here.


def index(request):
    return render_to_response("index.html")


def logout_view(request):
    logout(request)
    # Redirect to a success page.


def login_view(request):
    print request.POST
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username=username, password=password)
    print username
    print 
    print user
    if user is not None:
        print "ok"
        if user.is_active:
            login(request, user)
            redirect('/home/blog')
        else:
            return HttpResponse("Your account is disabled.")
    else:
        error_message='The username and password were incorrect.'
        return render_to_response('login.html', {"error_message":error_message}, context_instance=RequestContext(request))


def article_list(request):
    articles_list =  Article.objects.all()
    paginator = Paginator(articles_list, 5) # Show 5 articles per page
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)
        
    return render_to_response('article_list.html', 
        {"articles":articles}
        )



