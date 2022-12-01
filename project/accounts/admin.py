from django.contrib import admin
from .models import User, NOK, Account, Transaction

# Register your models here.

admin.site.register(User)
admin.site.register(NOK)
admin.site.register(Account)
admin.site.register(Transaction)

