# Create your models here.
import datetime

from django.db import models

currentDateTime = datetime.datetime.now()


def validName(title):
    return bool(not title or title.isspace())


class Course(models.Model):
    title = models.CharField(max_length=200, null=False)
    createdDate = models.DateField(auto_now_add=True)
    createdBy = models.CharField(max_length=200, null=True)

    def __unicode__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=200, null=False)
    embededLink = models.URLField()
    createdDate = models.DateField(auto_now_add=True)
    createdBy = models.CharField(max_length=200, null=True)

    def __unicode__(self):
        return self.title


class Chapter(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    weekNumber = models.IntegerField()

    def __unicode__(self):
        return self.title


class ContentVideo(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.PROTECT)
    orderPosition = models.IntegerField()


class ContentQuestion(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    # video = models.ForeignKey(Video,on_delete=models.PROTECT)
    orderPosition = models.IntegerField()
