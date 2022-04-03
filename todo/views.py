from django.shortcuts import redirect, render
from .models import ToDo
# Create your views here.
def index(request):
    todos=ToDo.objects.all()
    if request.method=="POST":
        print(request.POST['due_date'],'due date')
        if request.POST['task']:
            print(request.POST['task'],'task')
            new_todo=ToDo(
                task=request.POST['task'],
                due_date=request.POST['due_date']
            )
            new_todo.save()
            return redirect('/')
    return render(request,'index.html',{'todos':todos})

def delete(request,id):
    todo=ToDo.objects.get(id=id)
    todo.delete()
    return redirect('/')

def edit(request,id):
    todo=ToDo.objects.get(id=id)
    editable="true"
    return redirect('/')