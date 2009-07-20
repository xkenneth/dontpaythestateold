#!/usr/bin/python

import sys
import datetime
import logging

from helper import prepare_messages

LOG_FILENAME = '/home/citizen/dontpaythestate/cron/log/notify.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO,)

sys.path.append('/home/citizen/')

today = datetime.datetime.now()

#setup the django environment
from django.core.management import setup_environ
from django.core.mail import send_mail

from dontpaythestate import settings
setup_environ(settings)

from dontpaythestate.remember.models import Subscription, InactiveUsers

logging.info("\n\nCommencing Send-Off @ %s" % today)

active_users = []

#collect the active users
for sub in Subscription.objects.all():
    try:
        InactiveUsers.objects.get(email_address=sub.email_address)
        logging.info("User %s is not currently active." % sub)
    except Exception:
        logging.info("User %s is active!" % sub)
        active_users.append(sub)

for user in prepare_messages(active_users):
    send_mail("Registration Renewal Reminder From dontpaythestate.com",
              user['message'],
              'noreply@dontpaythestate.com',
              [user['email']], fail_silently=False)
