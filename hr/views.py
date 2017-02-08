from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from hr.serializers import *
from django.http import HttpResponse
import datetime
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.schemas import SchemaGenerator
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import response

def index(request):
    return HttpResponse("Hello Tangeneer!")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def detail(request, tangeneer_id):
    template = "hr/detail.html"

    context = {'tangeneer': 'Someones details'}

    return render(request, template, context)
    # return HttpResponse("You're looking at Tangeneer %s." % tangeneer_id)

class JobViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """
    # The Viewset needs to know how to retrieve our items
    queryset = Job.objects.all()

    # It also needs to know how to serialize what it finds
    serializer_class = JobSerializer # Serilizer to handle the data

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class SkillViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows skills to be viewed or edited.
    """
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

@api_view()
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
def schema_view(request):
    # Pass urlconf so only hr modules urls are registered
    generator = SchemaGenerator(title='Jobs API', urlconf=('hr.urls'),)
    return response.Response(generator.get_schema(request=request))
