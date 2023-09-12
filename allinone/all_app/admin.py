from django.contrib import admin
from all_app.models import *

# Register your models here.
admin.site.register(administrator)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Staff)
admin.site.register(Appointment)
admin.site.register(Department)