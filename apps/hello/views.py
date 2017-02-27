from django.shortcuts import render
# from .models import Person


# Create your views here.
def detail(request):
    return render(request, "hello/person.html") 
# person = Person.objects.first()
   
