from django.shortcuts import render, redirect
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

def query_person_by_name(req):
    print(Person.objects.filter(name=req.POST['name']))
    context = {
        'persons': Person.objects.filter(name=req.POST['name'])
    }
    return render(req, 'show_person.html', context)

def query_person_by_age(req):
    print(req.POST)
    print(Person.objects.filter(age=req.POST['age']))
    context = {
        'persons': Person.objects.filter(age=req.POST['age'])
    }
    return render(req, 'show_person.html', context)

def query_person_by_id(req):
    print(req.POST)
    print(Person.objects.filter(id=req.POST['id']))
    context = {
        'persons': Person.objects.filter(id=req.POST['id'])
    }
    return render(req, 'show_person.html', context)

def edit_person(req, pk):
    context = {
        'person': Person.objects.get(pk=pk)
    }
    return render(req, 'edit_person.html', context)

def apply(req, pk):
    person = Person(id=pk, name=req.POST['new_name'], age=req.POST['new_age'])
    person.save()
    return redirect('/')