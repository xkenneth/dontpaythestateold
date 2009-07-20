from django.db import models

# Create your models here.
class Subscription(models.Model):
    email_address = models.EmailField(max_length=100,primary_key=True)
    year = models.IntegerField()
    month = models.IntegerField()
    
    def __unicode__(self):
        return self.email_address

class InactiveUsers(models.Model):
    email_address = models.EmailField(max_length=100)
    uid = models.CharField(max_length=32,primary_key=True)
    
    def __unicode__(self):
        return self.email_address
    



