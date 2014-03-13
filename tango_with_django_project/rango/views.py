from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import RequestContext


def index(request):
    #context = RequestContext(request)
   # context_dict{'boldmessage': "I am from the context"}
    return HttpResponse("hello hehe")

# Create your views here.
