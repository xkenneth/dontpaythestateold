import datetime

def prepare_messages(users):

    today = datetime.datetime.now()

    year = today.year - 2000
    month = today.month

    messages = []
    
    for user in users:
        t = {}
        if user.year > 2000:
            t['year'] = user.year - 2000
        else:
            t['year'] = user.year
    
        t['months'] = (year - t['year']) * 12
            
        t['months'] += month - user.month
    
        if abs(t['months']) > 1:
            plural = 's'
        else:
            plural = ''

        if t['months'] > 0:
            t['message'] = "Your registration renewal was due %d month%s ago." % (t['months'],plural)
        elif t['months'] < 0:
            t['message'] = "Your registration renewal is due in %d month%s." % (abs(t['months']),plural)
        else:
            t['message'] = "Your registration renewal is due this month!"

        t['email'] = user.email_address

        if t['months'] < 3 and t['months'] > -3:
            messages.append(t)

    return messages

            



if __name__ == '__main__':
    #setup the django environment
    import sys

    sys.path.append('/home/citizen/')
    
    from django.core.management import setup_environ
    from django.core.mail import send_mail
    
    from dontpaythestate import settings
    setup_environ(settings)
    
    from dontpaythestate.remember.models import Subscription, InactiveUsers

    active_users = []
    
    #collect the active users
    for sub in Subscription.objects.all():
        try:
            InactiveUsers.objects.get(email_address=sub.email_address)
        except Exception:
            active_users.append(sub)

    
    print "Active Users Message Summary:"
    for user in prepare_messages(active_users):
        print user['email'],user['months']
