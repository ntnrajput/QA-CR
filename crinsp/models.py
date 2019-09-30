from django.db import models
import datetime
from django.contrib.auth.models import User
from django.conf import settings

class Testing(models.Model):
    Testing_Date = models.DateField(auto_now=False)
    RSM ='RSM'
    URM = 'URM'
    A ='A'
    B='B'
    C='C'
    R60 ='UIC-60'
    R52 ='IRS-52'
    P ='Pass'
    F ='Fail'
    Shift_Choice=[(A,'A'),(B,'B'),(C,'C')]
    Testing_Shift = models.CharField(max_length=1,choices=Shift_Choice,)
    Mill_Choice =[(RSM, 'RSM'), (URM,'URM')]
    Rolling_Mill = models.CharField(max_length=3,choices=Mill_Choice,default=RSM)
    Section_Choice =[(R60,'UIC-60'),(R52,'IRS-52')]
    Rail_Section = models.CharField(max_length=6,choices=Section_Choice,default=R60)
    IE_Testing = models.ForeignKey(User, on_delete=models.CASCADE)  
    
    Testing_Result_Choice =[(P,'Pass'),(F,'Fail')]
    Testing_Result = models.CharField(max_length =4, choices=Testing_Result_Choice,default=P)


    verbose_name_plural = "Testing Details"

    def __str__(self):
        return '%s   %s' %(self.Testing_Date, self.Testing_Shift)

class Heat_Status(models.Model):
    Heat_Number=models.CharField(max_length=6)
    Testing_Detail=models.ForeignKey(Testing,null=True,on_delete=models.CASCADE)
    verbose_name_plural = "Heat Status"
    def __str__(self):
        return '%s   %s' %(self.Heat_Number, self.Testing_Detail.Testing_Result)




  
