from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import FountainPenForm, NibForm
from .models import FountainPen, Nib 

def showAllFountainPens(request):

    fpens = FountainPen.objects.all()
    fpens_list = [fpen for fpen in fpens]

    context = {
        'fpens_list' : fpens_list
    }
    return render(request,'fountainpens/all_fountainpens.html',context)

def addNewFountainPen(request):
    form = FountainPenForm(request.POST) 

    if request.method == 'POST':
        form = FountainPenForm(request.POST)
        if form.is_valid():
            form.save()
            pen_model = form.cleaned_data.get("pen_model")
            messages.success(request,f'{pen_model} Has been added Successfully!')
            return redirect('showAllFountainPens')
        else:
            form = FountainPenForm()
    return render(request,'fountainpens/add_new_fountainpen.html',{'form': form})


def showAllNibs(request):
    nibs = Nib.objects.all()
    nibs_list = [nib for nib in nibs]
    context = {
        'nibs_list' : nibs_list
    }
    return render(request,'fountainpens/all_nibs.html',context)

def addNewNib(request):
    form = NibForm(request.POST) 

    if request.method == 'POST':
        form = NibForm(request.POST)
        if form.is_valid():
            form.save()
            nib_size = form.cleaned_data.get("nib_size")
            messages.success(request,f'{nib_size} Nib has been added Successfully!')
            return redirect('showAllNibs')
        else:
            form = NibForm()
    return render(request,'fountainpens/add-new-nib.html',{'form': form})
