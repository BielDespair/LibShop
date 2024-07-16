from django.db import models
from random import choices
from string import ascii_letters
# Create your models here.

def generate_code():
    length = 8

    while True:
        code = choices(ascii_letters,k=length)
        print(code)
        if not Room.objects.filter(code=code).count:
            return code
        
        
class Room(models.Model):
    created_at = models.DateField(auto_now=True)
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=20, unique=True)
