from rest_framework import serializers
from accounts.models import User, NOK, Account, Transaction

        
class UserNOKSerializer(serializers.ModelSerializer):
    # PrimaryKeyRelatedField
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=False) #user id i.e. 1
    class Meta:
        model = NOK
        fields='__all__'

class AccountSerializer(serializers.ModelSerializer):
    # PrimaryKeyRelatedField
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=False) #user id i.e. 1
    class Meta:
        model = Account
        fields='__all__'

class TransactionSerializer(serializers.ModelSerializer):
    # PrimaryKeyRelatedField
    transaction = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all(),many=False) #user id i.e. 1
    class Meta:
        model = Transaction
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    # PrimaryKeyRelatedField
    # tasks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    nok = UserNOKSerializer(read_only=True,many=True)
    class Meta:
        model = User
        fields='__all__'