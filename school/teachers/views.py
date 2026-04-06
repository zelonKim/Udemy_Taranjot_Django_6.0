from django.shortcuts import render
from .forms import TeachersForm
from django.http import HttpResponseRedirect, HttpResponse
from .models import Teacher


def home(request):
    if request.method == 'POST':
        form = TeachersForm(request.POST)
        if form.is_valid():         
            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # phone_number = form.cleaned_data['phone_number']
            # bio = form.cleaned_data['bio']
            
            # teacher = Teacher.objects.create(name=name, 
            #                                  email=email, 
            #                                  phone_number=phone_number,
            #                                  bio=bio)
            
            form.save()
            return HttpResponseRedirect('/teacher/thank-you/')
    else:
        form = TeachersForm()
    return render(request, 'teachers/home.html', {'form':form })



def thank(request):
    return HttpResponse("Form 제출완료")


def data(request):
    alldata = Teacher.objects.all()
    print(request.COOKIES['name'])
    return render(request, 'teachers/alldata.html', {'alldata': alldata})


def update(request, id):
    teacher = Teacher.objects.get(id=id)
    if request.method == 'POST':
        form = TeachersForm(request.POST, instance=teacher)
        if form.is_valid():
            # teacher.name = form.cleaned_data['name']
            # teacher.email = form.cleaned_data['email']
            # teacher.phone_number = form.cleaned_data['phone_number']
            # teacher.bio = form.cleaned_data['bio']
            teacher.save()
            return HttpResponseRedirect('/teacher/all-data/')
    else:   
        # form = TeachersForm(initial={'name': teacher.name, 'email':teacher.email, 'phone_number':teacher.phone_number, 'bio':teacher.bio})
        form = TeachersForm(instance=teacher)
    return render(request, 'teachers/update.html', {'form': form})



def delete(request, id):
    if request.method == 'POST':
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
    return HttpResponseRedirect('/teacher/home/')