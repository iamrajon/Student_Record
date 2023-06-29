from django.contrib import admin
from core.models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'email',
        'roll',
        'address',
    ]
    search_fields = ('name',)

admin.site.register(Student, StudentAdmin)

