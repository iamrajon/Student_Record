from django.shortcuts import render, redirect
from core.forms import StudentCreationForm
from .models import Student
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.

#function based view for student creation
def student_view(request):
    if request.method == "POST":
        fm = StudentCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Student Created Successfully!')
            return redirect('create-student')
        else:
            messages.error(request, 'Error Creating Student!')
    else:
        fm = StudentCreationForm()
        all_stud = Student.objects.all().order_by('-date_created')

        #pagination
        paginator = Paginator(all_stud, 7)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
    context = {'form':fm, 'student':page_obj}

    return render(request, "core/index.html", context)

# function based view for deleting student records
def delete_student(request, id):
    if request.method == "POST":
        target_stud = Student.objects.get(pk = id)
        target_stud.delete()
        messages.success(request, "Student Deleted Successfully!")
        return redirect('create-student')
    else:
        pass


# function based view for Editing Student Record 
def edit_student(request, id):
    if request.method == "POST":
        target_student = Student.objects.get(pk=id)
        fm = StudentCreationForm(request.POST, instance=target_student)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Student Data Updated Successfully!")
            return redirect('create-student')
        else:
            messages.error(request, "Error Updating Student Data!")
    else:
        target_student = Student.objects.get(pk=id)
        fm = StudentCreationForm(instance=target_student)
    
    context = {'form':fm}
    return render(request, 'core/update.html', context)

