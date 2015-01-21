from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'students/$',
        views.StudentListCreateAPIView.as_view(), name='students_list'),

    url(r'students/(?P<pk>[0-9]+)/$',
        views.StudentRetrieveUpdateDestroyAPIView.as_view(), name='students_detail'),
)
