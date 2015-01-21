from rest_framework.test import APITestCase

from students.tests.factories import StudentFactory


class TestStudentViewSet(APITestCase):

    def test_student_list(self):
        """Should return the list of all students when requesting /api/students"""
        for _ in range(2):
            StudentFactory()
        resp = self.client.get('/api/students/?format=json')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 2)

    def test_student_retrieve(self):
        """Should return the student matching given 'pk' when requesting /api/students/<pk>"""
        StudentFactory(pk=1, first_name='Martin')
        resp = self.client.get('/api/students/1/?format=json')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['first_name'], 'Martin')
