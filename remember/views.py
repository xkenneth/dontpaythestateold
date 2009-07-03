from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.core.urlresolvers import reverse
from dontpaythestate.remember.models import *

# Create your views here.
def index(request):
    print dir(request)
    
    t = loader.get_template('index.html')
    c = Context({})
    
    return HttpResponse(t.render(c))

def unsubscribe(request):
    t = loader.get_template('unsubscribe.html')
    c = Context({})
    
    return HttpResponse(t.render(c))

def removed(request):
    
    try:
        Subscription.objects.get(pk=request.POST['email']).delete()
    except:
        return HttpResponse("Email not subscribed!")
    
    return HttpResponse("Removed!")

def thanks(request):
    return HttpResponse("Thanks!")    

