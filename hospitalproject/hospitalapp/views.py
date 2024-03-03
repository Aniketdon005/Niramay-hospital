from django.shortcuts import render,redirect,HttpResponse
from hospitalapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

# this is home views code
def base(request): 
    
    return render(request,'base.html')

# this is contact views code

def contact(request):
    
    if (request.method == "GET"):
        
    
        return render(request,'contact.html')
    
    else:
        
        cname = request.POST['cname']
        cemail = request.POST['cemail']
        cmobile = request.POST['cmobile']
        cage = request.POST['cage']
        cgender = request.POST['cgender']
        caddress = request.POST['caddress']
        
        m = contact1.objects.create(cname = cname,cemail = cemail,cmobile = cmobile,cage = cage,cgender = cgender,caddress = caddress)
        m.save()
        
        return render(request,'contact.html')

# this is logout views code

def userlogout(request):
    
    logout(request)
    
    return render(request,'logout.html')

# this is signin views code

def usersignin(request):
    
    if(request.method == 'GET'):
    
        return render(request,'signin.html')
    
    else:
        
        luser = request.POST['luser']
        lpass = request.POST['lpass']
        
        m = authenticate(username = luser, password = lpass)
        
        if(m is not None):
            
            login(request,m)
            
            return redirect('/base')
        
        else:
            
            return HttpResponse("username or password incorrect")

# this is signup views code

def usersignup(request):
    
    if(request.method == 'GET'):
    
        return render(request,'signup.html')
    
    else:
        
        rfname = request.POST['rfname']
        rlname = request.POST['rlname']
        runame = request.POST['runame']
        remail = request.POST['remail']
        rpass = request.POST['rpass']
        rcpass = request.POST['rcpass']
        #raddress = request.POST['raddress']
        
        if rfname == "" or rlname == "" or remail == "" or runame == "" or rpass == "" or rcpass == "" :
            
            context = {}
            context['msg'] = "field can not be empty"
            
            return render(request,'signup.html',context)
        
        else:
        
            m = User.objects.create(first_name = rfname ,last_name = rlname,username = runame,email = remail)#address = raddress)
            m.set_password(rpass)
            m.set_password(rcpass)
            m.save()
        
        if(rpass == rcpass):
            
            context = {}
            context['msg'] = 'password and confirm password are not same'
            
            return render(request,'signup.html',context)
        
        else:
            
            return render(request,'signup.html')
        
def paitentdashboard(request):
    
    m = User.objects.all()
    
    context = {}
    context['data'] = m
    
    
    return render(request,'paitentdashboard.html',context)