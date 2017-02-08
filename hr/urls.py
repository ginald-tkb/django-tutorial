from django.conf.urls import url, include
from rest_framework import routers
from . import views
from hr.views import schema_view

router = routers.DefaultRouter()
router.register(r'jobs', views.JobViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'skills', views.SkillViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^datetime/$', views.current_datetime, name='current_datetime'),
    url(r'^(?P<tangeneer_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^api/', include(router.urls)),
    url(r'^api-explorer/', schema_view),
]
