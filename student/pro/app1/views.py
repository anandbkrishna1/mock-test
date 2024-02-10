from django.shortcuts import render
from .models import students
# Create your views here.
def index(request):
    content=students.objects.all()
    data={
        'student':content
    }
    return render(request,'student.html',data)


def detail(request,id):
    person=students.objects.get(pk=id)
    print(person)
    data={
        'data':person
    }
    return render(request,'detail.html',data)
