from django.shortcuts import redirect, render
from django.http import HttpResponse
from student.models import *


# Create your views here.

def all_students(request):
    if request.method == "GET":
        students = Student.objects.all()
        context = {
            'all_students': students
        }
        return render(request, 'student/home.html', context)

    elif request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]

        Student.objects.create(name=name, email=email)

        return redirect('/')


def action_handler(request, action, sid):
    if action == 'delete':
        # Get the student to be deleted
        student = Student.objects.get(id=sid)

        # Delete the student
        student.delete()

    elif action == 'edit':
        if request.method == 'GET':
            student = Student.objects.get(id=sid)

            context = {
                'student': student,
            }
            return render(request, 'student/edit.html', context)

        if request.method == 'POST':
            # Get the form data
            input_name = request.POST["name"]
            input_email = request.POST["email"]

            # Get the student to be edited
            student = Student.objects.get(id=sid)

            # Update the student
            student.name = input_name
            student.email = input_email

            # Save the student to the database
            student.save()

    return redirect('/')
