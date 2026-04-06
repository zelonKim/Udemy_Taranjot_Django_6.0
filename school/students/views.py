from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.shortcuts import render

def set(request):
    # raise Exception("예외 발생!")
    # response = render(request, "students/home.html")
    response = TemplateResponse(request, "students/home.html", {'name':'Taranjot'})
    response.set_cookie('theme', 'dark', max_age=600, httponly=True)
    response.set_cookie('name', 'Rahul')
    return response


def get(request):
    theme = request.COOKIES['theme']
    return HttpResponse(f"<h1>This is Get Page.</h1>{theme}")


def delete(request):
    response = HttpResponse("This is Delete Page")
    response.delete_cookie("name")
    return response


def update(request):
    response = HttpResponse('<h1>This is Update Page</h1>')
    response.set_cookie('names', 'Simar')
    return response


