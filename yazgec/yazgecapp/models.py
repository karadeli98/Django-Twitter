from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    surname =  models.CharField(max_length=100)
    userName =  models.CharField(max_length=100)
    password =  models.CharField(max_length=2000)
    email = models.EmailField(max_length=100)
    userId = models.AutoField(primary_key=True)

    def __str__(self):
        return self.userName

class Post(models.Model):
    postId = models.AutoField(primary_key=True)
    context = models.CharField(max_length=240)
    ownerUsername = models.CharField(max_length=100)

    def __str__(self):
        return self.context[:20]

class friendShip(models.Model):
    user1 = models.CharField(max_length=100)
    user2 = models.CharField(max_length=100)

    def __str__(self):
        return self.user1 + "->" + self.user2
    

