# Create your models here.
import datetime

from django.db import models

currentDateTime = datetime.datetime.now()


def validName(title):
    return bool(not title or title.isspace())


class Course(models.Model):
    title = models.CharField(max_length=200, null=False)
    createdDate = models.DateField()
    createdBy = models.CharField(max_length=200, null=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        print("hello world")
        if self.createdDate is None:
            self.createdDate = currentDateTime
        if validName(self.title):
            raise Exception("title name should be valid")
        return super().save(*args, **kwargs)


class Chapter(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        print("hello")
        if validName(self.title):
            raise Exception("title name should be valid")
        return super().save(*args, **kwargs)
