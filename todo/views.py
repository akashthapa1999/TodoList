from django.shortcuts import render , HttpResponseRedirect
from .forms import TodoForm
from .models import TodoModel

# Create your views here.


def home(request):
    md = TodoModel.objects.all()
    if request.method == "POST":
        fm = TodoForm(request.POST)
        if fm.is_valid():    
            dt = fm.cleaned_data["Title"]
            reg = TodoModel(Title=dt)
            reg.save()
            fm = TodoForm()
    else:
        fm = TodoForm()
        md = TodoModel.objects.all()
        
    return render (request, "index.html", {"form":fm ,"todo":md})


def delete(request, id):
    if request.method =="POST":
        pi = TodoModel.objects.get(pk=id)
        pi.delete()

        return HttpResponseRedirect("/")
    

def update(request, id):
    if request.method=="POST":
        pi = TodoModel.objects.get(pk=id)
        fm = TodoForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/")

    else:
        pi = TodoModel.objects.get(pk=id)
        fm = TodoForm(instance=pi)

    return render(request, "update.html", {'form':fm})




