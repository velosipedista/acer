from django.shortcuts import render
from db.models import Person

def enter(req):
    name = req.POST['name']
    age = req.POST['age']
    p = Person(name=name, age=age)
    p.save()
    return render(req, 'enter.html')

def show_list(req):
    context = {
        'list' : Person.objects.all(),
    }
    return render(req, 'list.html', context)