from django.contrib import admin

from .models import Banner,About,Portfolio
# Register your models here.
class AdminBanner(admin.ModelAdmin):
    list_display=('Id','Title','Description' ,'Image')

class AdminAbout(admin.ModelAdmin):
    list_display=('Id','Title','Description' ,'Image')

class AdminPortfolio(admin.ModelAdmin):
    list_display=('Id','Title','Description' ,'Image')

admin.site.register(Banner,AdminBanner)
admin.site.register(About,AdminAbout)
admin.site.register(Portfolio,AdminPortfolio)