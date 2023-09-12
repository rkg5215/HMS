from django.contrib import admin
from django.urls import path
from all_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('welcome/', views.welcome, name='welcome'),
    path('index/', views.index, name='index'),
    path('logout/', views.logout, name='logout'),

    path('departments/', views.departments, name='departments'),
    path('add_department/', views.add_department, name='add_department'),
    path('update_department/<int:id>', views.update_department, name='update_department'),
    path("delete_department/<int:id>", views.delete_department, name='delete_department'),

    path('doctors/', views.doctors, name='doctors'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    path('edit_doctor/', views.edit_doctor, name='edit_doctor'),
    path('update_doctor/<int:id>', views.update_doctor, name='update_doctor'),
    path("delete_doctor/<int:id>", views.delete_doctor, name='delete_doctor'),

    path('patients/', views.patients, name='patients'),
    path('add_patient/', views.add_patient, name='add_patient'),
    # path('edit_patient/', views.edit_patient, name='edit_patient'),
    path('update_patient/<int:id>', views.update_patient, name='update_patient'),
    path("delete_patient/<int:id>", views.delete_patient, name='delete_patient'),

    path('staff/', views.staffs, name='staffs'),
    path('add_staff/', views.add_staff, name='add_staff'),
    path('update_staff/<int:id>', views.update_staff, name='update_staff'),
    path("delete_staff/<int:id>", views.delete_staff, name='delete_staff'),
    path("checkbox_staff/<str:id>", views.checkbox_staff, name='checkbox_staff'),

    path('appointments/', views.appointments, name='appointments'),
    path('add_appoinment/', views.add_staff, name='add_appointment'),
    path('update_appointment/<int:id>', views.update_staff, name='update_appointment'),
    path("delete_appointment/<int:id>", views.delete_staff, name='delete_appointment'),

]



