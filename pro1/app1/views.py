from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student
# Create your views here.
def add_view(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name='app1/add.html'
    context={'form':form}
    return render(request,template_name,context)

def show_view(request):
    obj=Student.objects.all()
    template_name='app1/show.html'
    context={'obj':obj}
    return render(request,template_name,context)

def update_view(request,pk):
    obj=Student.objects.get(roll=pk)
    form=StudentForm(instance=obj)
    if request.method== 'POST':
        form=StudentForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name='app1/add.html'
    context={'form':form}
    return render(request,template_name,context)

def delete_view(request,pk):
    obj=Student.objects.get(roll=pk)
    if request.method=='POST':
        obj.delete()
        return redirect('show_url')
    template_name='app1/delete.html'
    context={'obj':obj}
    return render(request,template_name,context)
