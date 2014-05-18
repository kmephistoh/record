from django.shortcuts import render_to_response
from blog.models import * 

# Create your views here.


def index(request):
	return render_to_response("index.html")


def article_list(request):
	articles =  Article.objects.all()
	return render_to_response('article_list.html', 
		{"articles":articles}
		)



