from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,Http404
from .models import Login
from .forms import User


def Home(request):
    if request.method=='POST':
        form=User(request.POST or None)
        if form.is_valid():
            form.save()
            form = User()

    else:
        form=User()
    try:
        login = Login.objects.all()
    except Login.DoesNotExist:
        raise Http404('Page not found')

    return render(request, "home.html", {'form':form,'login':login,})

def Update(request, id):
    if request.method=='POST':
        ud=Login.objects.get(pk=id)
        form=User(request.POST, instance=ud)
        if form.is_valid():
            form.save()
            form=User()
    else:
        ud = Login.objects.get(pk=id)
        form = User(instance=ud)

    return render(request, "view.html",{'form':form})
'''
def Update(request, id):
    if request.method=='POST':
        ud=Login.objects.get(pk=id)
        form=User(request.POST, instance=ud)
        if form.is_valid():
            form.save()
            form=User()
    else:
        ud = Login.objects.get(pk=id)
        form = User(instance=ud)
    
    return render(request, "home.html", {'form': form})
'''

def Delete(request,id):
    #if request.method =='POST':
    dl=Login.objects.get(pk=id)
    dl.delete()
    return HttpResponseRedirect('/')

#add comment


