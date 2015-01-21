from rest_framework import generics

from students.models import Student
from .serializers import StudentSerializer


class StudentMixin(object):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    paginate_by = 10


class StudentListCreateAPIView(StudentMixin, generics.ListCreateAPIView):
    pass


class StudentRetrieveUpdateDestroyAPIView(StudentMixin,
                                          generics.RetrieveUpdateDestroyAPIView):
    pass
