from django.db import models

# Create your models here.

class User(models.Model):
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length= 25)
    userName = models.CharField(max_length=25)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=15)
    # password = models.CharField(max_length=6, null=True, default=None)
    hashed_otp = models.CharField(max_length=25, null=True, default=None)  # Modify the field length as needed



    def __str__(self):
        return self.userName

