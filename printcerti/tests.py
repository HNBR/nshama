from django.test import TestCase
from .models import Person


class TestPersonModel(TestCase):

    def test_creating_person(self):
        payload = {
            "first_name": "حسن",
            "medium_name": "بشير",
            "last_name": "مياه حسين"
        }
        test_person = Person.objects.create(**payload)
        test_person.save()

        self.assertEqual(test_person.first_name, payload["first_name"])
        self.assertEqual(test_person.medium_name, payload["medium_name"])
        self.assertEqual(test_person.last_name, payload["last_name"])
