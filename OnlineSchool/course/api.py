from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from course.models import Course, Chapter, Video, ContentQuestion, ContentVideo


class CourseResource(ModelResource):
    class Meta:
        authorization = Authorization()
        queryset = Course.objects.all()
        resource_name = 'course'

class VideoResource(ModelResource):
    class Meta:
        authorization = Authorization()
        queryset = Video.objects.all()
        resource_name = 'video'


class ReadOnlyCourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'course'
        filtering = {
            'id': ALL,
        }

class ReadOnlyChapterResource(ModelResource):
    class Meta:
        queryset = Chapter.objects.all()
        resource_name = 'chapter'
        filtering = {
            'id': ALL,
        }

class ReadOnlyVideoResource(ModelResource):
    class Meta:
        queryset = Video.objects.all()
        resource_name = 'video'
        fields = ['title','embededLink']
        filtering = {
            'id': ALL,
        }


class ChapterResource(ModelResource):
    course = fields.ForeignKey(ReadOnlyCourseResource, 'course', full=True)

    class Meta:
        authorization = Authorization()
        queryset = Chapter.objects.all().order_by('weekNumber').select_related('course')
        resource_name = 'chapter'
        filtering = {
            'course': ALL_WITH_RELATIONS,
            'weekNumber': ALL,
        }

class ContentVideoResource(ModelResource):
    chapter = fields.ForeignKey(ReadOnlyChapterResource, 'chapter', full=True)
    video = fields.ForeignKey(ReadOnlyVideoResource, 'video', full=True)

    class Meta:
        authorization = Authorization()
        queryset = ContentVideo.objects.all().order_by('orderPosition').select_related('chapter')
        resource_name = 'contentVideo'
        filtering = {
            'chapter': ALL_WITH_RELATIONS,
        }

class ContentQuestionResource(ModelResource):
    chapter = fields.ForeignKey(ReadOnlyChapterResource, 'chapter', full=True)

    class Meta:
        authorization = Authorization()
        queryset = ContentQuestion.objects.all().order_by( 'orderPosition').select_related('chapter')
        resource_name = 'contentQuestion'
        filtering = {
            'chapter': ALL_WITH_RELATIONS,
        }
