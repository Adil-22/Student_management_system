from django.shortcuts import render,HttpResponseRedirect
from .forms import student_form
from .models import Students


def show_data(request):
   
   if request.method == 'POST':
     form = student_form(request.POST)
     if form.is_valid():
   
      nm = form.cleaned_data['name']                       
      fn =  form.cleaned_data['father_name']                
      ph =  form.cleaned_data['phone']                      
      em =   form.cleaned_data['email']                     
      add =  form.cleaned_data['address']                   
      
      reg=Students(name=nm,father_name=fn,phone=ph,email=em,address=add)
      reg.save()
      form=student_form()
   else:
       form=student_form()
   student =Students.objects.all()  
   return render(request,"home.html",{"form":form,"stu":student})




def update_data(request,id):
   if request.method == 'POST':
      pi = Students.objects.get(pk=id)
      form=student_form(request.POST, instance=pi)
      if form.is_valid():
          form.save()
      

   else:
      pi=Students.objects.get(pk=id)
   form=student_form(instance=pi) 


   return render (request,"update.html",{"form":form})






def delete_data(request,id):
   if request.method =='POST':
      pi = Students.objects.get(pk=id)
      pi.delete()
      return HttpResponseRedirect("/")

   

   
   
