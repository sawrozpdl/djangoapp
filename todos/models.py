from django.db import models
from utils.random import genId
from django.utils import timezone


class User(models.Model):
    uid = models.CharField(blank=True,default=genId, primary_key=True, max_length=12)
    userName = models.CharField(max_length=128)
    email = models.EmailField()
    password = models.CharField(max_length=64)
    deletedAt = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return "{uid} => {userName}".format(uid=self.uid, userName=self.userName)


class Todo(models.Model):
    tid = models.CharField(blank=True, default=genId, primary_key=True, max_length=12)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    title = models.CharField(max_length=128)
    content = models.TextField(max_length=65000)
    dateCreated = models.DateTimeField(default=timezone.now)
    dateModified = models.DateTimeField(default=timezone.now)
    deletedAt = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return "{tid} => {title} by : {userName}".format(tid=self.tid, title=self.title, userName=self.user.userName)
