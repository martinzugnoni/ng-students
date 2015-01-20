from rest_framework.test import APITestCase

from students.tests.factories import StudentFactory


class TestStudentViewSet(APITestCase):

    def test_student_retrieve(self):
        """Should return a media object when it belongs to the given account"""
        for _ in range(2):
            StudentFactory()
        resp = self.client.get('/api/students/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 2)
