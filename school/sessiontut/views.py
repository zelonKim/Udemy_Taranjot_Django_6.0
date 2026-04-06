from django.shortcuts import render
from django.http import HttpResponse

def set(request):
    request.session['name'] = {'name1': 'Simar', 'name2': 'Rahul'}
    request.session['fatherName'] = 'Daniel'
    # request.session.set_expiry(10)
    return HttpResponse("Hello World")


def get(request):
    name = request.session['name']
    father_name = request.session['fatherName']
    print(name) # John
    print(father_name) # Daniel
    print(request.session.get_expiry_age()) # 10
    return HttpResponse(f'<h1>GET VIEW</h1>{name} and {father_name}')


def delete(request):
    request.session.flush()
    request.session.clear_expired()
    # del request.session['name']
    # del request.session['fatherName']
    return HttpResponse("<h1>Delete View</h1>")


def update(request):
    request.session['name']['name1'] = 'John'
    request.session.modified = True
    return HttpResponse("update page")