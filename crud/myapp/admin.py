from django.contrib import admin

from  .models import Students 

@admin.register(Students)
class Student_admin(admin.ModelAdmin):
    list_display=('id','name','father_name','phone','email','address')


    def __str__(request):
        return request.name


