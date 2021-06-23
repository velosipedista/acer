from django.shortcuts import render
from db.models import Person


def index(req):
    return render(req, 'index.html')

def create(req):
    return render(req, 'create.html')




