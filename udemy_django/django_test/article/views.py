from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

# Create your views here.


def hello(request):
    name = "Mike"
    html = "<html><body>Hi %s, this seems to have worked!</body></html>" % name
    return HttpResponse(html)
