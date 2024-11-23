from django.db import models

# Create your models here.
class StudentRegister(models.Model):  
    name = models.CharField(max_length=100)  
    mobile = models.CharField(max_length=15) 
    email = models.EmailField()  

    class Meta:  
        db_table = "tblemployee"