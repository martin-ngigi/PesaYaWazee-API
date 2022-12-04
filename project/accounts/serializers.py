from rest_framework import serializers
from accounts.models import User, NOK, Account, Transaction

'''
DESCRPTION
-Every user two nested objects:
    -Next of Kin(NOK)
    -Account
-Every Account has Transaction

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



class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields='__all__'


class AccountSerializer(serializers.ModelSerializer):
    transaction = TransactionSerializer(read_only=True, many=True)
    class Meta:
        model = Account
        fields='__all__'


class UserNOKSerializer(serializers.ModelSerializer):
    class Meta:
        model = NOK
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    nok = UserNOKSerializer(read_only=True,many=True)
    account = AccountSerializer(read_only=True,many=True)
    class Meta:
        model = User
        fields='__all__'