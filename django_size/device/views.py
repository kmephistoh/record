# Create your views here.
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from device.models import * 

# Create your views here.


def index(request):
    return render_to_response("index.html")


def device_list(request):
    # device_router = DeviceRouterForm()
    device_router =  DeviceRouter.objects.all()
    # paginator = Paginator(device_list, 5) # Show 5 articles per page
    # page = request.GET.get('page')
    # try:
    #     device_router = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     device_router = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     device_router = paginator.page(paginator.num_pages)
        
    print device_router
    return render_to_response('device_list.html', 
        {"device_router":device_router}
        )
