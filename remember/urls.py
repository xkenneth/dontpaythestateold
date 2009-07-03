from django.conf.urls.defaults import *
from dontpaythestate.remember.forms import *

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.create_update.create_object',
     {'form_class': SubscriptionForm,
      'template_name': 'generic_form.html',
      'post_save_redirect':'thanks',
      }
     ),

    (r'^unsubscribe', 'dontpaythestate.remember.views.unsubscribe'),
     
    (r'^signup', 'dontpaythestate.remember.views.signup'),

    (r'^thanks', 'dontpaythestate.remember.views.thanks'),
                       
    (r'^removed', 'dontpaythestate.remember.views.removed'),

    )
