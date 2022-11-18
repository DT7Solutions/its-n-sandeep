from django.shortcuts import render
from .models import Banner,About,Portfolio
# Create your views here.
def home(request):
    banner_item = Banner.objects.all()
    about_item = About.objects.all()
    portitem_item = Portfolio.objects.all()
    return render(request, 'uifiles/index.html',{'banner_item':banner_item, 'about_item':about_item,'portitem_item':portitem_item})