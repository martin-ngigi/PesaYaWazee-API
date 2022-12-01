from django.db import models

# Create your models here.

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
    
    class Meta:
        ordering=('nationId',)
        
    def __str__(self):
        return self.idNumber +' '+ self.firstName

# The UserImmunization model holds a ManyToOne relationship with the User model
# The same immunization will not be assigned to more than one user, but one user can have multiple immunizations.
# Hence, the UserImmunizationSerializer class should serialize only a single user instance, whereas, UserSerializer class should serialize one or more userimuniserializer instances (more than one immunization can be assigned to an user). 
class NOK(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    idNumber = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=20)
    user = models.ForeignKey(User,related_name='nok',on_delete=models.CASCADE) #NB: "user", "immunizations" must be the same as the one used in the serializers

    class Meta:
        ordering = ('idNumber',)

    def __str__(self):
        return self.idNumber +' '+ self.firstName

class Account(models.Model):
    user = models.ForeignKey(User,related_name='account',on_delete=models.CASCADE) #NB: "user", "immunizations" must be the same as the one used in the serializers
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
    account = models.ForeignKey(Account,related_name='transaction',on_delete=models.CASCADE) #NB: "user", "immunizations" must be the same as the one used in the serializers
    timeStamp = models.DateTimeField(auto_now_add=True)
    amount = models.CharField(max_length=50)
    teller = models.CharField(max_length=50)
    transactionStatus = models.CharField(blank=True, max_length=50)

    class Meta:
        ordering = ('code',)
    def __str__(self):
        return self.code