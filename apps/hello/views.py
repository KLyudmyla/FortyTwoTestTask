from django.shortcuts import render
from .models import Person


# Create your views here.
def detail(request):
#    person = Person.objects.first()
    return render(request, "hello/person.html")
