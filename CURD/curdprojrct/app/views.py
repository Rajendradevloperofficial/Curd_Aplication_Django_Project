from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .forms import data_register
from .models import register
from django.views.decorators.csrf import csrf_exempt 


# insert new data  and show data
@csrf_exempt
def add_show(request):
    if request.method=='POST':
        fm = data_register(request.POST, request.FILES)
        if fm.is_valid():
            nm= fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pa= fm.cleaned_data['password']
            img = fm.cleaned_data['screenshot']
            reg = register(name=nm, email=em, password=pa,screenshot=img)
            reg.save()
        fm=data_register()
    else:      
        fm=data_register()
    data=register.objects.all()
        
    return render(request,'addshow.html',{'form':fm,'data':data})

#delete data one by one
# @csrf_exempt
def delete_data(request,id):
    if request.method=='POST':
        pi =register.objects.get(pk=id)
        pi.delete()
       
        return HttpResponseRedirect('/')
    
#update all data
def update(request,id):
    if request.method=='POST':
        pi=register.objects.get(pk=id)
        fm=data_register(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
       
    else:
        pi=register.objects.get(pk=id)
        fm=data_register(instance=pi)
       
    return render(request,'update.html',{'form':fm})