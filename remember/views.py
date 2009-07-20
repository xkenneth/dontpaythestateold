from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.core.urlresolvers import reverse
from dontpaythestate.remember.models import *

# Create your views here.
def index(request):
    t = loader.get_template('index.html')
    c = Context({})
    
    return HttpResponse(t.render(c))

def unsubscribe(request):
    t = loader.get_template('unsubscribe.html')
    c = Context({})
    
    return HttpResponse(t.render(c))

def removed(request):    
    t = loader.get_template('thanks.html')
    
    c = Context({})
    
    try:
        Subscription.objects.get(pk=request.POST['email']).delete()
    except:
        t = loader.get_template('notsubscribed.html')
    
    return HttpResponse(t.render(c))

def thanks(request):
    t = loader.get_template('thanks.html')
    c = Context({})
    
    return HttpResponse(t.render(c))

def activate(request, uid):
    InactiveUsers.objects.get(pk=uid).delete()

    t = loader.get_template('thanks.html')
    c = Context({})
    
    return HttpResponse(t.render(c))
