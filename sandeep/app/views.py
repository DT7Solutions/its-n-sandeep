from django.shortcuts import render
from .models import Banner,About,Portfolio ,Contact,OurClientReview,BrandSlider
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def home(request):
    banner_item = Banner.objects.all()
    about_item = About.objects.all()
    portitem_item = Portfolio.objects.all()
    brand_logo = BrandSlider.objects.all()
    ourClients = OurClientReview.objects.all()
    #Contact 
    if request.method == "POST":
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        message = request.POST.get('message',"")
        
        oContactinfo = Contact(Name=name,Email=email,Message=message)
        oContactinfo.save()
    
        sucess =f'hi {name} sucessfully Sending email'
        subject = 'it s n sandeep'
        message ='''
        Subject:{}
        Message:{}
        From:{}
        '''.format(subject,message,email)
        try:
            send_mail(subject, message,'noreplaybadugudinesh94@gmail.com',recipient_list=['badugudinesh94@gmail.com']) 
            messages.success(request,sucess)
        except:
            messages.error(request,'your emsil sending fail')

    return render(request, 'uifiles/index.html',{'banner_item':banner_item, 'about_item':about_item,'portitem_item':portitem_item,'brand_logo':brand_logo,'ourClients':ourClients})