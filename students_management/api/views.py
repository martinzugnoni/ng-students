from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response

from students.models import Student
from .serializers import StudentSerializer


class StudentsViewSet(viewsets.ViewSet):

    def list(self, request):
        """Returns the whole list of students"""
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Creates a new student based on POSTed data"""
        serializer = StudentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        Student.objects.create(**serializer.data)
        return Response(status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        """Returns the student matchin given 'pk' value"""
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """(PUT) Updates the whole student object"""
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        student.__dict__.update(**serializer.data)
        student.save()
        return Response(status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        """(PATCH) Updates partial fields of the student object"""
        pass

    def destroy(self, request, pk=None):
        """Deletes the student object with given 'pk' value"""
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return Response(status=status.HTTP_200_OK)
