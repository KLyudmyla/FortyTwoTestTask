from django.test import TestCase, Client
from. models import Person


# Create your tests here.
class PersonDetailTest(TestCase):
    class Meta:
        model = Person
    
    def test_pages_person_detail_200(self):
        client = Client()
        person1 = Person.objects.create(
                               name="Lyuda",
                               surname="Kaluzhynova",
                               bio="biography",
                               date_birth='1980-06-14',
		               email='vlyuda@mail.ru',
                               jabber='lyudmyla@22cc.co',
                               skype='kaluzhynoval',
			       )
        response=client.get('/')
        self.assertEqual(response.status_code, 200)


    def test_person_detail(self):
        client = Client()
        person1 = Person.objects.create(
                               name="Lyuda",
                               surname="Kaluzhynova",
                               bio="biography",
                               date_birth='1980-06-14',
		               email='vlyuda@mail.ru',
                               jabber='lyudmyla@22cc.co',
                               skype='kaluzhynoval', 
                                  )
        response = client.get('/')
        self.assertContains(response, 'Lyudmyla')
        self.assertContains(response, "Kaluzhynova")
        self.assertContains(response, "biography")


    def test_pages_person_empty(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "42 Coffee Cups Test Assignment")
        self.assertContains(response, "Name")
        self.assertContains(response, "Last name")


class SomeTests(TestCase):
    def test_math(self):
        "put docstrings in your tests"
        assert(2 + 2 == 4)
