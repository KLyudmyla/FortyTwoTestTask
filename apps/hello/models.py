from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')
    surname = models.CharField(max_length=255, verbose_name='surname')
    date_birth = models.DateField(null=True)
    bio = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    skype = models.CharField(max_length=255, blank=True)
    jabber = models.CharField(max_length=255, blank=True)
    other_contacts = models.TextField(blank=True)
    def __str__(self):
        return self.name


