from django.contrib.auth.models import User
from django.db import models

from accounts.choices import USERROLE

# Create your models here.

class UserProfile(models.Model):
    user_role = models.IntegerField(choices=USERROLE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    address1 = models.CharField(max_length=100, null=True, blank=True)
    pin = models.CharField(max_length=10, null=True, blank=True)
    additional_email = models.TextField(null=True, blank=True)
    count = models.IntegerField(null=True, blank=True, default=0)
    blocktime = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=False)
    reset_password = models.CharField(max_length=100, null=True, blank=True)
    buying_email = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
            return self.company