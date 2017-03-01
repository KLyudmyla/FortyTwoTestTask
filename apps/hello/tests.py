from django.test import TestCase, Client
from. models import Person


# Create your tests here.
class PersonDetailTest(TestCase):
    class Meta:
        model = Person

    def test_pages_person_detail_200(self):
        """
        Test for working template
        """
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_person_detail(self):
        """
        checking info in the template
        """
        client = Client()
        response = client.get('/')
        self.assertContains(response, 'Lyudmyla')
        self.assertContains(response, "Kaluzhynova")
        self.assertContains(response, "biography")
        self.assertContains(response, '06-02-1980')
        self.assertContains(response, "kaluzhynova@gmail.com")
        self.assertContains(response, "klyudmyla@42cc.co")
        self.assertContains(response, 'klyudmyla')
        self.assertContains(response, "Other contacts")
        self.assertContains(response, "Name")
        self.assertContains(response, 'Last name')
        self.assertContains(response, "Date of birth")
        self.assertContains(response, "bio")
        self.assertContains(response, 'Contacts')
        self.assertContains(response, "Email")
        self.assertContains(response, "Jabber")
        self.assertContains(response, 'Skype')
        self.assertContains(response, "Other contacts")

    def test_pages_person_empty(self):
        """
        checking template with empty DB
        """
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
