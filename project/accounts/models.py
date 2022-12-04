from django.db import models

# Create your models here.

'''
DESCRPTION
-Every user two nested objects:
    -Next of Kin(NOK)
    -Account
-Every Account has several Transaction

eg:
user{
    nok{

    }
    account{
        transaction{
            
        }
    }
}
'''

# Link https://www.geeksforgeeks.org/serializer-relations-django-rest-framework/

STATUSALIVE = (('A','Alive'),('D','Dead'),)
STATUS = (('A','Active'),('I','InActive'),)

class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    idNumber = models.CharField(max_length=20)
    dob = models.CharField(max_length=20)
    residence = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=20)
    nationId = models.CharField(max_length=20)
    status = models.CharField(max_length=1,choices=STATUSALIVE,default='A')
    kra = models.CharField(max_length=30)
    imageIDFront = models.ImageField(upload_to='images', blank=True, null=True) 
    imageIDBack = models.ImageField(upload_to='images', blank=True, null=True)  
    
    class Meta:
        ordering=('nationId',)
        
    def __str__(self):
        return self.idNumber +' '+ self.firstName

class NOK(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    idNumber = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=20)
    user = models.ForeignKey(User,related_name='nok',on_delete=models.CASCADE) 

    class Meta:
        ordering = ('idNumber',)

    def __str__(self):
        return self.idNumber +' '+ self.firstName

class Account(models.Model):
    user = models.ForeignKey(User,related_name='account',on_delete=models.CASCADE) 
    acc_number = models.CharField(max_length=50)
    status = models.CharField(max_length=1,choices=STATUS,default='I')
    balance = models.CharField(max_length=20)

    class Meta:
        ordering = ('acc_number',)
    def __str__(self):
        return self.acc_number

class Transaction(models.Model):
    import uuid
    uuid = uuid.uuid1()
    
    code = models.CharField(default=uuid, max_length=50)
    account = models.ForeignKey(Account,related_name='transaction',on_delete=models.CASCADE)
    timeStamp = models.DateTimeField(auto_now_add=True)
    amount = models.CharField(max_length=50)
    teller = models.CharField(max_length=50)
    transactionStatus = models.CharField(blank=True, max_length=50)

    class Meta:
        ordering = ('code',)
    def __str__(self):
        return self.code