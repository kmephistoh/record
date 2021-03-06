from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import Context
from django.views.generic.base import TemplateView

from article.models import Article
# Create your views here.


def hello(request):
    name = "Mike"
    html = "<html><body>Hi %s, this seems to have worked!</body></html>" % name
    return HttpResponse(html)


def hello_template(request):
    name = "Anti maga"
    t = get_template("hello.html")
    html = t.render(Context({'name': name}))
    return HttpResponse(html)


def hello_template_simple(request):
    name = "kaer"
    return render_to_response("hello.html", {'name': name})


class HelloTemplate(TemplateView):
    template_name = "hello.html"

    def get_context_data(self, **kwargs):
        context = super(HelloTemplate, self).get_context_data(**kwargs)
        context['name'] = "pugna"
        return context


def articles(request):
    return render_to_response('articles.html',
                              {'articles': Article.objects.all()})


def article(request, article_id=1):
    return render_to_response('article.html',
                              {'article': Article.objects.get(id=article_id)})
