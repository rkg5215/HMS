from django.shortcuts import render, redirect, reverse
from django.shortcuts import HttpResponse
from all_app.models import *
from all_app import models

from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required


def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_list= models.administrator.objects.filter(username= username)

        error_name=[]
        if user_list:
            error_name='The user name already exists'

            return render (request, 'register.html',{'error_name': error_name})
        else:
            username=models.administrator.objects.create(username=username, password=password,email=email)
            username.save()

        return redirect('/login')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        obj_user = models.administrator.objects.filter(username=username, password=password)
        if obj_user:
            request.session["uid"]=request.POST.get('username')
            messages.success(request, "Login Successfully.")
            return redirect('/index')
        error = 'Wrong username and password'

    return render(request, "login.html", locals())  #--locals() passed to render() is to send all local variables of the view



def index(request):
    if request.session.has_key('uid'):
        user_name = (request.session["uid"]).capitalize()
        return render(request, "index.html", locals())
    else:
        return redirect('/login')


def logout(request):
    try:
        del request.session["uid"]
    except KeyError:
        pass
    return redirect("/login")

def welcome(request):
    return render(request, "welcome.html")


def main(request):
    return render(request, "main.html")

def departments(request):
    if request.session.has_key('uid'):
        user_name = (request.session["uid"]).capitalize()
        department_list = Department.objects.all()
        context = {
            'department_list': department_list,
            'user_name': user_name
        }
        return render(request, "department.html", context)
    return redirect("/login")

def add_department(request):
    if request.method=='POST':
        department_name=request.POST.get('department_name')
        department_description = request.POST.get('department_description')
        entry=Department(
            department_name = department_name,
            department_description = department_description,
        )
        entry.save()
        return redirect("/departments")

def update_department(request,id):
    if request.method =='POST':
        department_name = request.POST.get('department_name')
        department_description = request.POST.get('department_description')

        entry = Department(
            id=id,
            department_name=department_name,
            department_description=department_description
        )
        entry.save()
        return redirect("/departments")

def delete_department(request,id):
    department = Department.objects.filter(id=id)
    department.delete()
    return redirect("/departments")

def doctors(request):
    if request.session.has_key('uid'):
        user_name = (request.session["uid"]).capitalize()
        doctor_list = Doctor.objects.all()
        context={
            'doctor_list':doctor_list,
            'user_name' : user_name
        }
        return render(request, "doctors.html", context)
    else:
        return redirect("/login")

def add_doctor(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        entry=Doctor(
            name = name,
            email = email,
            address= address,
            phone=phone
        )
        entry.save()
        return redirect("/doctors")


def edit_doctor(request):
    doctor_list = Doctor.objects.all()
    context = {
        'doctor_list': doctor_list
    }
    return render(request, "doctors.html", context)

def update_doctor(request,id):
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        entry=Doctor(
            id=id,
            name = name,
            email = email,
            address= address,
            phone=phone
        )
        entry.save()
        return redirect("/doctors")

def delete_doctor(request,id):
    doctor = Doctor.objects.filter(id=id)    #--You Can also use :- doctor = Doctor.objects.get(id=id)
    doctor.delete()
    return redirect("/doctors")

def patients(request):
    if request.session.has_key('uid'):
        user_name = (request.session["uid"]).capitalize()
        patient_list = Patient.objects.all()
        # patient_list = Patient.objects.all().order_by('name')  # --This is for alphabetic order(Assecending), for decending('-name')
        # patient_list = Patient.objects.all().order_by('name')[:3] # For slicing only 3 entry show
        context = {
            'patient_list': patient_list,
            'user_name': user_name
        }
        return render(request, "patients.html", context)
    return redirect("/login")

def add_patient(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        entry = Patient(
            name = name,
            email = email,
            address= address,
            phone=phone
        )
        entry.save()
        return redirect("/patients")

# def edit_patient(request):
#     patient_list = Patient.objects.all()
#     context = {
#         'patient_list': patient_list
#     }
#     return render(request, "patients.html", context)

def update_patient(request,id):
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        entry=Patient(
            id=id,
            name = name,
            email = email,
            address= address,
            phone=phone
        )
        entry.save()
        return redirect("/patients")

def delete_patient(request,id):
    patient = Patient.objects.filter(id=id)
    patient.delete()
    return redirect("/patients")

def staffs(request):
    if request.session.has_key('uid'):
        user_name = (request.session["uid"]).capitalize()
        staff_list = Staff.objects.all()
        context = {
            'staff_list': staff_list,
            'user_name': user_name
        }
        return render(request, "staff.html", context)
    else:
        return redirect("/login")

def add_staff(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        entry=Staff(
            name = name,
            email = email,
            address= address,
            phone=phone
        )
        entry.save()
        return redirect("/staff")


def update_staff(request,id):
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        entry=Staff(
            id=id,
            name = name,
            email = email,
            address= address,
            phone=phone
        )
        entry.save()
        return redirect("/staff")

def delete_staff(request,id):
    staff = Staff.objects.filter(id=id)
    staff.delete()
    return redirect("/staff")

def checkbox_staff(request,id):

    new = request.POST['options']
    print(new)


def appointments(request):
    if request.session.has_key('uid'):
        user_name = (request.session["uid"]).capitalize()
        appointment_list = Appointment.objects.all()
        print(appointment_list)
        print(appointment_list)
        context = {
            'appointment_list': appointment_list,
            'user_name': user_name
        }
        return render(request, "appointment.html", context)
    else:
        return redirect("/login")

def add_appointment(request):
    if request.method=='POST':
        patient_name=request.POST.get('patient_name')
        doctor_name = request.POST.get('doctor_name')
        date_time = request.POST.get('date_time')
        entry=Appointment(

            patient_name = patient_name,
            doctor_name = doctor_name,
            date_time= date_time,
        )
        entry.save()
        return redirect("/appointments")


# def update_appointment(request,id):
#     if request.method =='POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         address = request.POST.get('address')
#         phone = request.POST.get('phone')
#         entry=Appointment(
#             id=id,
#             name = name,
#             email = email,
#             address= address,
#             phone=phone
#         )
#         entry.save()
#         return redirect("/appointments")
#
# def delete_appointment(request,id):
#    appointment = Appointment.objects.filter(id=id)
#    appointment.delete()
#     return redirect("/appointments")
