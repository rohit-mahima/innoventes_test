from tracemalloc import start
from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator, RegexValidator


class Company(models.Model):
    """class for comapny containing details"""
    companyName=models.TextField(max_length=120,null=False,
                                validators=[MinLengthValidator(5,'the filed must contain at least 5 char')])#name of company , mandatory, not null

    emailId=models.EmailField(null=False) #email field mandatory filed

    companyCode=models.CharField(max_length=5, unique=True, validators=[MinLengthValidator(5,'the filed must contain at least 5 char'),RegexValidator('^[a-zA-Z]{2}[0-9]{2}(E|N)$','the combination is wrong')]) #containing comapny code
                               
    Strength=models.PositiveIntegerField(default=0)#strength of comany having all positive values

    website=models.URLField() # urls field
    
    created_time=models.DateTimeField(null=False,default=timezone.now()) #date and time when data is created

    def __str__(self):
        return self.companyName