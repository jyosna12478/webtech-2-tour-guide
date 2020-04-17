from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import datetime



GENDER_CHOICES = (('M','Male'),('F','Female'))
CATEGORY_CHOICES = (('B','Family Tours'),('R','Religious Tours'),('S','Solo Trips'),('A','Adventure Trips'))
class Enquiry1(models.Model):
	Name = models.CharField(max_length = 50)
	Gender = models.CharField(choices = GENDER_CHOICES,max_length = 128,default = 'M')
	dob = models.DateField(max_length = 8)
	age = models.IntegerField()
	phone = models.CharField(max_length= 12)
	Email = models.EmailField(max_length = 70,blank = True)
	Category = models.CharField(choices = CATEGORY_CHOICES,max_length = 128)
	No_of_Days = models.IntegerField()
	No_of_Childrens = models.IntegerField()
	No_of_Adults = models.IntegerField()
	Enquiry_message = models.TextField()

	def __unicode__(self):
		return u'%s %s' % (self.Name,self.Gender)
class Category(models.Model):
	name=models.CharField(max_length=50)

class Packagess(models.Model):
	category = models.ForeignKey(Category,on_delete=models.CASCADE)
	real_category=models.CharField(max_length=50)
	subcategory = models.CharField(max_length=200)
	packages = models.CharField(max_length=200)
	price = models.PositiveIntegerField()
	information = models.TextField()

"""class Doctors(models.Model):
    doctors = models.CharField(max_length=50)"""
    
