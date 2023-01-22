from django.shortcuts import render, redirect, HttpResponseRedirect
from . import models
from . import forms

# Create your views here.


def err(request):
    return render(request,'error.html')

# Course App Home Page function:
def home(request):
    all_courses = models.Course.objects.all()
    return render(request, "courseapp/index.html", {"courses": all_courses})



# Add_New Page view function:
def addnew(request):
    cForm = forms.CourseForm()
    return render(request, "courseapp/addnew.html", {"blankForm": cForm})


# Save Data function:
def savedata(request):
    if request.method == "POST":
        varForm = forms.CourseForm(request.POST)
        if varForm.is_valid():
            try:
                varForm.save()
            except:
                pass
        else:
            return redirect(err)
    return redirect(home)



# Edit Page view function:
def edit(request,id):
    course_match = models.Course.objects.get(id=id)
    varEditForm = forms.CourseForm(instance=course_match)
    return render(request, "courseapp/edit.html", {"editForm": varEditForm, "course_obj": course_match})

# Save_Updated_Data function:
def update(request,id):
    course_match = models.Course.objects.get(id=id)
    if request.method == "POST":
        uForm = forms.CourseForm(request.POST, instance=course_match)
        if uForm.is_valid():
            try:
                uForm.save()
            except:
                pass
        else:
            return redirect(err)
    return redirect(home)



# Delete_Data function:
def dlt(request, id):
    course_match = models.Course.objects.get(id=id)
    course_match.delete()
    return redirect(home)






