from rest_framework.test import APITestCase

from students.tests.factories import StudentFactory

from students.models import Student


class TestStudentViewSet(APITestCase):

    def test_student_list(self):
        """Should return the list of all students when requesting /api/students"""
        for _ in range(2):
            StudentFactory()
        resp = self.client.get('/api/students/?format=json')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data['results']), 2)

    def test_student_retrieve(self):
        """Should return the student matching given 'pk' when requesting /api/students/<pk>"""
        StudentFactory(pk=1, first_name='Martin')
        resp = self.client.get('/api/students/1/?format=json')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['first_name'], 'Martin')

    def test_student_create(self):
        """Should create a new student when given data is valid"""
        data = {'first_name': 'Martin', 'last_name': 'Livesay',
                'email': 'martin.livesay@something.com',
                'date_of_birth': '2013-02-12'}
        resp = self.client.post('/api/students/', data=data)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(Student.objects.count(), 1)

    def test_student_create_invalid_data(self):
        """Should return 400 and not create the student when given data is not valid"""
        data = {'invalid': 'data'}
        resp = self.client.post('/api/students/', data=data)
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(Student.objects.count(), 0)

    def test_student_destroy(self):
        """Should delete the student with given 'pk' when /api/students/<pk> is requested with DELETE"""
        StudentFactory(pk=1)
        resp = self.client.delete('/api/students/1/')
        self.assertEqual(resp.status_code, 204)
        self.assertEqual(Student.objects.count(), 0)

    def test_student_destroy_not_found(self):
        """Should return 404 and do not delete any student when no student was found with given 'pk' value"""
        StudentFactory(pk=1)
        resp = self.client.delete('/api/students/10/')
        self.assertEqual(resp.status_code, 404)
        self.assertEqual(Student.objects.count(), 1)

    def test_student_update(self):
        """Should update the student when all student data is provided"""
        StudentFactory(pk=1, first_name='Martin', email='a@a.com')
        data = {'first_name': 'Ivan', 'last_name': 'Livesay',
                'email': 'ivan.livesay@something.com',
                'date_of_birth': '2013-02-12'}
        resp = self.client.put('/api/students/1/', data=data)
        self.assertEqual(resp.status_code, 200)
        student = Student.objects.get(pk=1)
        self.assertEqual(student.first_name, 'Ivan')
        self.assertEqual(student.email, 'ivan.livesay@something.com')

    def test_student_update_invalid_data(self):
        """Should return 400 when given data is invalid or not complete"""
        StudentFactory(pk=1, first_name='Martin', email='a@a.com')
        data = {'invalid': 'data'}
        resp = self.client.put('/api/students/1/', data=data)
        self.assertEqual(resp.status_code, 400)

    def test_student_update_not_found(self):
        """Should return 404 when there's no student matching with given 'pk' value"""
        StudentFactory(pk=1, first_name='Martin', email='a@a.com')
        resp = self.client.put('/api/students/10/', data={})
        self.assertEqual(resp.status_code, 404)

    def test_student_partial_update(self):
        """Should update only given fields when PATCH method is used"""
        StudentFactory(pk=1, first_name='Martin')
        data = {'first_name': 'Ivan'}
        resp = self.client.patch('/api/students/1/', data=data)
        self.assertEqual(resp.status_code, 200)
        student = Student.objects.get(pk=1)
        self.assertEqual(student.first_name, 'Ivan')

    def test_student_partial_update_invalid_data(self):
        """Should return 400 when given data is invalid"""
        StudentFactory(pk=1, first_name='Martin', email='a@a.com')
        data = {'date_of_birth': True}
        resp = self.client.patch('/api/students/1/', data=data)
        self.assertEqual(resp.status_code, 400)

    def test_student_partial_update_not_found(self):
        """Should return 404 when there's no student matching with given 'pk' value"""
        StudentFactory(pk=1, first_name='Martin', email='a@a.com')
        resp = self.client.patch('/api/students/10/', data={})
        self.assertEqual(resp.status_code, 404)
