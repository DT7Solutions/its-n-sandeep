from django.db import models

# Create your models here.
class Banner(models.Model):
        Id = models.IntegerField(primary_key = True)
        Title = models.CharField(max_length=25,default="heading")
        Description = models.CharField(max_length=100)
        Image = models.ImageField(upload_to='uploads/')
        def __str__(self):
            return self.Title


class About(models.Model):
        Id = models.IntegerField(primary_key = True)
        Title = models.CharField(max_length=25,default="heading")
        Description = models.CharField(max_length=2000)
        Image = models.ImageField(upload_to='uploads/')
        def __str__(self):
            return self.Title

class Portfolio(models.Model):
        Id = models.IntegerField(primary_key = True)
        Title = models.CharField(max_length=25,default="heading")
        Description = models.CharField(max_length=100)
        Image = models.ImageField(upload_to='uploads/')
        def __str__(self):
            return self.Title