from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False,
                                     blank=True, null=True)

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name).title()
