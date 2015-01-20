from datetime import date

from django.test import TestCase

from ..models import Student
from .factories import StudentFactory


class TestStudentModel(TestCase):

    def test_student_create(self):
        """Should create a new Student object"""
        Student.objects.create(first_name='John', last_name='Lennon',
                               date_of_birth=date.today(),
                               email='john.lennon@something.com')
        self.assertEqual(Student.objects.count(), 1)

    def test_student_full_name_property(self):
        """Should return the concatenation of first and last name when full_name is asked"""
        StudentFactory(first_name='Martin', last_name='Evan')
        student = Student.objects.get(first_name='Martin')
        self.assertEqual(student.full_name, 'Martin Evan')
