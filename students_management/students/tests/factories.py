import random
from datetime import date, timedelta

import factory

from ..models import Student

FIRST_NAMES = ['Charline', 'India', 'Ashlie', 'Sterling', 'Faustino', 'Layla',
               'Starr', 'Leisa', 'Dodie', 'Erinn']

LAST_NAMES = ['Cashin', 'Imai', 'Alverez', 'Salcido', 'Fanning', 'Lipps',
              'Stelle', 'Livesay', 'Dentler', 'Evan']


class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Student

    first_name = factory.Sequence(lambda n: random.choice(FIRST_NAMES))
    last_name = factory.Sequence(lambda n: random.choice(LAST_NAMES))
    email = factory.LazyAttribute(
        lambda a: '{}.{}@foobar.com'.format(a.first_name, a.last_name).lower())
    date_of_birth = date.today() - timedelta(days=30 * 12 * 18)  # 18 years old
