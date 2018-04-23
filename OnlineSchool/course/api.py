from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource

from course.models import Course, Chapter


class CourseResource(ModelResource):
    class Meta:
        authorization = Authorization()
        queryset = Course.objects.all()
        resource_name = 'course'


class ReadOnlyCourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'course'


class ChapterResource(ModelResource):
    course = fields.ForeignKey(ReadOnlyCourseResource, 'course', full=True)

    class Meta:
        authorization = Authorization()
        queryset = Chapter.objects.all()
        resource_name = 'chapter'
