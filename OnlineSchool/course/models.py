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
        if self.createdDate is None:
            self.createdDate = currentDateTime
        if validName(self.title):
            raise Exception("title name should be valid")
        return super().save(*args, **kwargs)


class Video(models.Model):
    title = models.CharField(max_length=200, null=False)
    embededLink = models.URLField()
    createdDate = models.DateField()
    createdBy = models.CharField(max_length=200, null=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
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
        if validName(self.title):
            raise Exception("title name should be valid")
        return super().save(*args, **kwargs)

class ContentVideo(models.Model):
    chapter = models.ForeignKey(Chapter,on_delete=models.CASCADE)
    video = models.ForeignKey(Video,on_delete=models.PROTECT)
    weekNumber = models.IntegerField()
    orderPosition = models.IntegerField()

class ContentQuestion(models.Model):
    chapter = models.ForeignKey(Chapter,on_delete=models.CASCADE)
   # video = models.ForeignKey(Video,on_delete=models.PROTECT)
    weekNumber = models.IntegerField()
    orderPosition = models.IntegerField()
