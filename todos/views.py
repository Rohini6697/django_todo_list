from datetime import date, datetime
from django.shortcuts import get_object_or_404, render,redirect
from .models import Events


# Create your views here.
def home(request):
    display_todos = Events.objects.all().values()
    false = Events.objects.all().filter(task_status = False).count()
   
    today = date.today()

    
    

    return render(request,'index.html',{'todo_events':display_todos,
                                        'false':false,
                                        'today':today})



def add(request):
    return render(request,'add.html')
def add_todo(request):
    tasks = request.POST['task']
    description = request.POST['description']
    due_date = request.POST['due']
    due_date = due_date if due_date else None

    today = date.today()
    if due_date:
        due_date = datetime.strptime(due_date,'%Y-%m-%d').date()
        if due_date < today:
            return render(request,'add.html',{'error':'that date already over'})
    new_task = Events(task = tasks,description = description,due_date = due_date,)
    if tasks and description and due_date:
        new_task.save()
    return redirect('home')
def delete_todo(request,id):
    todo = Events.objects.all().get(id=id)
    todo.delete()
    return redirect('home')
# def update(request,id):
    
#     return render(request,'update.html',{'todo':todo})
def update_todo(request,id):
    todo = get_object_or_404(Events,id=id)
    if request.method == 'POST':
        tasks = request.POST.get('task')
        description = request.POST.get('description')
        due_date_str = request.POST.get('due')
        # due_date = due_date if due_date else None
        status = 'status' in request.POST        
       
        due_date=None
        today = date.today()
        if due_date_str:
            due_date = datetime.strptime(due_date_str,'%Y-%m-%d').date()
            if due_date < today:
                return render(request,'update.html',{'error':'that date already over'},)#'todo': todo,'task_value': tasks,'description_value': description,'due_value': due_date_str#





        # due_date = None
        # if due_date_str:
        #     due_date = datetime.strptime(due_date_str,'%Y-%m-%d').date()
        #     today = date.today()
        #     if due_date < today:
        #         return render(request,'add.html',{'error':'that date already over'})



        
            


        todo.task = tasks
        todo.description = description
        todo.due_date = due_date
        todo.task_status = status
        todo.save()
        return redirect('home')
    return render(request,'update.html',{'todo':todo})

