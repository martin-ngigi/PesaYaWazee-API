from django.shortcuts import render

# Create your views here.

# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from accounts.models import User, NOK, Account, Transaction
from accounts.serializers import UserSerializer, UserNOKSerializer, AccountSerializer, TransactionSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters
from rest_framework.views import APIView

from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework import viewsets
from rest_framework import generics

# # MY SIMPLE APIVIEW
class UserView(APIView):
    # List all snippets, or create a new snippet.
    def get(self, request):
        users = User.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = UserSerializer(users, many=True)
        return Response({"users": serializer.data})

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# SERACH BY EMAIL OR PHONE.(can GET, POST,SEARCH)
class UsersList(generics.ListCreateAPIView):
    # eg: http://127.0.0.1:8000/user-by-email-or-phone?search=martinwainaina001@gmail.com
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter]
    search_fields = ['idNumber', 'kra']

# SERACH BY immunizationName
class NOKLists(generics.ListCreateAPIView):
    queryset = NOK.objects.all()
    serializer_class = UserNOKSerializer
    filter_backends = [SearchFilter]
    search_fields = ['idNumber']


class AccountLists(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    filter_backends = [SearchFilter]
    #search_fields = ['idNumber']

class TransactionLists(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = [SearchFilter]
    #search_fields = ['idNumber']