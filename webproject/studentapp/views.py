from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.
def home(request):
    studentsD = Student.objects.all()
    return render(request,'studentapp/index.html', {'students':studentsD})




def addnew(request):
    blankForm = StudentForm()
    return render(request,'studentapp/addnew.html', {'blankFormS': blankForm})


def savedata(request):
    if request.method == "POST":
        stform = StudentForm(request.POST)
        if stform.is_valid():
            stform.save()
    return redirect(home)


def edit(request,id):
    var = Student.objects.get(id=id)
    instan = StudentForm(instance=var)
    return render(request, 'studentapp/edit.html', {'viewForm':instan, "st":var})

def update(request, id):
    var = Student.objects.get(id=id)
    if request.method == "POST":
        stform = StudentForm(request.POST, instance=var)
        if stform.is_valid():
            try:
                stform.save()
            except:
                pass
    return redirect(home)




def rem(request,id):
    var = Student.objects.get(id=id)
    var.delete()
    return redirect(home)









