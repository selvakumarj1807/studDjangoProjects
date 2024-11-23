from django.shortcuts import redirect, render

from projectApp.forms import StudentRegisterForm

# Create your views here.

def index(request):
    form = StudentRegisterForm()
    return render(request,'regForm.html',{'form':form})

def addnew(request):
    if request.method == "POST":  
        form = StudentRegisterForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass
    else:  
        form = StudentRegisterForm()
    return render(request,"regForm.html",{'form':form})
