from django.shortcuts import render,redirect
from.forms import *
from django.db.models import Q
from django.core.mail import EmailMessage,send_mail,BadHeaderError
from django.views.generic.edit import FormView

from django.contrib import messages
from django.conf import settings
# Create your views here.
def index_view(request):
    if request.method=="POST":
        district=request.POST['district']
        blood=request.POST['blood']
        print('dfdsf')
        obj=BloodBank.objects.filter(Q(bloodgroup__contains=blood),district=district) 
        obj2=Person.objects.filter(Q(bloodgroup__contains=blood),district=district)  
        print(obj)
        return render(request,'search.html',{'obj':obj,'obj2':obj2})
    else:
        print('yo yo')
        
    return render(request,'index.html',{})

def middle_view(request):


    return render(request,'middle.html',{})

def person_view(request):

    if request.method=="POST":
        form=PersonForm(request.POST)
        if form.is_valid():
            form.create_person()
            return redirect('index')
        else:
            print(form.errors)
            print('failed')
    else:
        form=PersonForm
    return render(request,'person.html',{'form':form})

def bloodbank_view(request):
    if request.method=="POST":
        form=BloodBankForm(request.POST)
        if form.is_valid():
            form.create_bloodbank()
            return redirect('index')
        else:
            print(form.errors)
            print('fail')
    else:
        form=BloodBankForm()
    return render(request,'bloodbank.html',{'form':form})

def list_view(request):
    obj=BloodBank.objects.all()
    if request.method=="POST":
        district=request.POST['district']
        
        print('dfdsf')
        obj=BloodBank.objects.filter(district=district) 
        
        print(obj)
        return render(request,'list.html',{'obj':obj})
    else:
        print('yo yo')
        
    return render(request,'list.html',{})
    
    return render(request,'list.html',{'obj':obj})


class ContactView(FormView):
    template_name="contact.html"
    form_class=ContactForm
    success_url="/contact/"

    def form_valid(self,form):
        name=form.cleaned_data.get('name')
        blood=form.cleaned_data.get('blood')
        phone=form.cleaned_data.get('phone')
        date=form.cleaned_data.get('date')
        from_email=form.cleaned_data.get('email')

        message_view="Thanks "+name+ " We got your mail.We will respond you as soon as possible"
        subject=name
        message="name: "+name+"\n"+ "blood group:" +blood+"\n"+"phone number: " +phone+"\n"+"date: " +date+"\n"+"email:"+from_email
        #send mail function
        send_mail(
            
            subject,
            message,
            #settings.EMAIL_HOST_USER,
            from_email,
            ['homerepairservice81@gmail.com'],
            fail_silently=False
        )
        messages.add_message(self.request, messages.INFO,message_view)
        return super(ContactView,self).form_valid(form)
