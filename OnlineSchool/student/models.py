from django.db import models
from course import models as cm

# Create your models here.


class Parent(models.Model):
    name = models.CharField(max_length=200, null=False)
    password = models.CharField(max_length =200, null= False)
    emailAddress = models.CharField(max_length=200, null=False)

    def __unicode__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=200, null=False)
    parent = models.ForeignKey(Parent, on_delete= models.PROTECT)
    password = models.CharField(max_length =200, null= False)
    emailAddress = models.CharField(max_length=200, null=False)

    def __unicode__(self):
        return self.name

class enrollmentState(models.Model):
    student = models.ForeignKey(Student,on_delete = models.CASCADE)
    course = models.ForeignKey(cm.Course, on_delete = models.PROTECT)
    chapter = models.ForeignKey(cm.Chapter,on_delete=models.PROTECT)

class completedContentVideo():
    contentVideo = models.ForeignKey(cm.ContentVideo, on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete = models.CASCADE)

class completedContentQuestion():
    contentQuestion = models.ForeignKey(cm.ContentQuestion, on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete = models.CASCADE)






