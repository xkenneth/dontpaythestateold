from django import forms
from django.forms import ModelForm
from dontpaythestate.remember.models import *

class SubscriptionForm(ModelForm):

    class Meta:
        model = Subscription
