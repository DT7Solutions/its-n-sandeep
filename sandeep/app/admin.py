from django.contrib import admin

from .models import Banner,About,Portfolio,Contact,BrandSlider,OurClientReview
# Register your models here.
class AdminBanner(admin.ModelAdmin):
    list_display=('Id','Title','Description' ,'Image')

class AdminAbout(admin.ModelAdmin):
    list_display=('Id','Title','Description' ,'Image')

class AdminPortfolio(admin.ModelAdmin):
    list_display=('Id','Title','Description' ,'Image')


class AdminContact(admin.ModelAdmin):
    list_display=('Id','Name','Email' ,'Message')


class AdminBrandSlider(admin.ModelAdmin):
    list_display=('Id','Image')

class AdminHappyClients(admin.ModelAdmin):
    list_display=('Id','Name','Message','Image')

admin.site.register(Banner,AdminBanner)
admin.site.register(About,AdminAbout)
admin.site.register(Portfolio,AdminPortfolio)
admin.site.register(Contact,AdminContact)
admin.site.register(BrandSlider,AdminBrandSlider)
admin.site.register(OurClientReview,AdminHappyClients)