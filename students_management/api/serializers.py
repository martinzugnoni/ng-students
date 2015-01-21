from rest_framework import serializers

from students.models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('pk', 'first_name', 'last_name', 'email', 'date_of_birth')
