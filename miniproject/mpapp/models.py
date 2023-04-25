from django.db import models

class Languages_offered(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')

class Langs(models.Model):
    name=models.CharField(max_length=250)
    name1=models.CharField(max_length=250)
    desc=models.CharField(max_length=250)

class Teachers(models.Model):
    name= models.CharField(max_length=250)
    lang= models.CharField(max_length=250)
    prof= models.CharField(max_length=250)
    rating= models.IntegerField()



class user_Registration(models.Model):
    name=models.CharField(max_length=100)
    lang=models.CharField(max_length=100)
    email=models.EmailField()
    phone= models.CharField(max_length=10)
    password= models.CharField(max_length=100)
    password1= models.CharField(max_length=100)

class Contact_us(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    message=models.TextField()

    def __str__(self):
        return self.name


