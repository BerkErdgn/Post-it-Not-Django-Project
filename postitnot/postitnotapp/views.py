from django.shortcuts import render,redirect

from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from . import models

# Create your views here.



def index(request):
    if request.user != "AnonymousUser":
        print(request.user)
        allNot = models.AddNot.objects.filter(Q(author=request.user)).all()
        return render(request, "postitnotapp/mainscreen.html",context={"allNot":allNot})
    else:
        return render(request, "postitnotapp/mainscreen.html")


@login_required(login_url="/login")
def subjectview(request,sybject):
    print(sybject)
    deneme = sybject
    allNot = models.AddNot.objects.filter(Q(author=request.user)).all()
    allSubjectNot = models.AddNot.objects.filter(Q(author=request.user) and Q(note_subject=deneme)).all()
    print(allSubjectNot)
    return render(request,"postitnotapp/subjectview.html",context={"allNot":allNot,"allSubjectNot":allSubjectNot})
    


@login_required(login_url="/login")
def addNot(request):
    allNot = models.AddNot.objects.filter(Q(author=request.user)).all()
    return render(request,"postitnotapp/addNot.html",context={"allNot":allNot})

@login_required(login_url="/login")
def postit(request):
    if request.POST:
        author = request.user
        data = request.POST
        note_subject=data['subject']
        note_title= data['title']
        note= data['note']
        models.AddNot.objects.create(author=author,note_subject=note_subject,note_title=note_title,note=note)
        return redirect("postitnotapp:index")
    
@login_required(login_url="/login")
def delete(request,pk):
    models.AddNot.objects.filter(author=request.user,id=pk)[0].delete()
    return redirect("postitnotapp:index")


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/singup.html"

