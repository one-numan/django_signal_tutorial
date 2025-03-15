from django.shortcuts import render,HttpResponse
from home import signals

# Create your views here.
def index_page(request):
    signals.notification.send(sender=None,request=request,user=["Numan","Marvel"])
    return HttpResponse("This is Index Page")