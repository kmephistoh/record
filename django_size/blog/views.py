from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import * 

# Create your views here.


def index(request):
    return render_to_response("index.html")


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



