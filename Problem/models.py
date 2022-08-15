from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator, RegexValidator

class Company(models.Model):
    companyName=models.TextField(max_length=120,null=False,
                                validators=[MinLengthValidator(5,'the filed must contain at least 5 char')])

    emailId=models.EmailField(null=False)

    companyCode=models.CharField(max_length=5, unique=True)# validators=[RegexValidator('^[a-zA-Z]{1,2}\[0-9]{1,2}\[E,N]')])
                               
    Strength=models.PositiveBigIntegerField()

    website=models.URLField()
    
    created_time=models.DateTimeField(null=False,default=timezone.now())

    def __str__(self):
        return self.companyName