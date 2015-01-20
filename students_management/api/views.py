from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from students.models import Student
from .serializers import StudentSerializer


class StudentsViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
