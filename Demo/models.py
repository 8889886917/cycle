from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

# Create your models here.
class indexP(models.Model):
     Tittle=models.CharField(max_length=10)
     Description=RichTextField() 
     Image=models.ImageField(upload_to='media/')
    
class aboutP(models.Model):
    Tittle=models.CharField(max_length=10) 
    Description=RichTextField()
    Image=models.ImageField(upload_to='media/')
    
class newsP(models.Model): 
    Tittle=models.CharField(max_length=10)
    Description=RichTextField()
    Image=models.ImageField(upload_to='media/')   
    
class contactP(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField()
    Number=models.TextField()
    Message=models.TextField()     
    
class cycleP(models.Model):
    Tittle=models.CharField(max_length=10)
    Description=RichTextField()
    Image=models.ImageField(upload_to='media/')  
    