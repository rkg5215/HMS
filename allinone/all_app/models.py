from django.db import models

class administrator(models.Model):

    username=models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=100)

    class Meta:
        db_table= "administrator"

    def __str__(self):
        return self.username

class Doctor(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=20)

    class Meta:
        db_table= "doctors"   #-- For table Name if not given table name as model name

    def __str__(self):
        return self.name

class Patient(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=20)

    class Meta:
        db_table= "patients"

    def __str__(self):
        return self.name

class Staff(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=20)

    class Meta:
        db_table= "staff"

    def __str__(self):
        return self.name

class Appointment(models.Model):

    # patient_name = models.ForeignKey(Patient, on_delete=models.CASCADE,default=1)
    patient_name = models.ManyToManyField(Patient)
    doctor_name = models.ManyToManyField(Doctor)
    date_time = models.DateTimeField(null=True)

    class Meta:
        db_table = "appointment"

    # First Way to return

    # def __str__(self):
    #     return '{}'.format(', '.join(self.patient_name.all().values_list('name', flat=True)))

    # Second Way to return

    def __str__(self):
        return self.patient_name.all().first().name


class Department(models.Model):

    department_name = models.CharField(max_length=100)
    department_description = models.CharField(max_length=300)

    class Meta:
        db_table= "department"

    def __str__(self):
        return self.department_name