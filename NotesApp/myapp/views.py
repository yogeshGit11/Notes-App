from django.shortcuts import render,HttpResponseRedirect
from django.views import View
from .models import mynotes
from .forms import noteform
from django.contrib import messages

# Create your views here.

def homepage(request):
    note=mynotes.objects.all()
    return render(request,'web/notes.html',{'note':note})

def addnotespage(request):
    if request.method=='POST':
        form=noteform(request.POST)
        if form.is_valid():
            topic=form.cleaned_data['topic']
            title=form.cleaned_data['title']
            note=form.cleaned_data['note']
    
            addnote=mynotes(topic=topic,title=title,note=note)
            addnote.save()
            form=noteform()
            
            messages.success(request,'Note has been added :)')

    else:
        form=noteform()

    return render(request,'web/addnotes.html',{'form':form})

def updatenotepage(request,id):
    if request.method=='POST':
        upid=mynotes.objects.get(pk=id)
        form=noteform(request.POST,instance=upid)
        if form.is_valid():
            form.save()
            form=noteform()
            messages.success(request,'Note has been Updated :)')

    else:
        upid=mynotes.objects.get(pk=id)
        form=noteform(instance=upid)

    return render(request,'web/update.html',{'form':form})

def deletenote(request,id):
    if request.method=='POST':
        delid=mynotes.objects.get(pk=id)
        delid.delete()

    return HttpResponseRedirect('/')

def contactpage(request):
    return render(request,'web/contact.html')

def aboutpage(request):
    return render(request,'web/about.html')