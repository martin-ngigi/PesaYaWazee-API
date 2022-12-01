from django.urls import path
from accounts import apiviews,views

urlpatterns = [

    # GET and POST
    path('users/', apiviews.UserView.as_view(),  name='Users'),
    # GET, PUT, DELETE
    path('users/<int:pk>/', apiviews.UserDetail.as_view(),  name='Users'),
    path('nok/', apiviews.NOKLists.as_view(),  name='Users'),
    path('account/', apiviews.AccountLists.as_view(),  name='Account'),
    path('transaction/', apiviews.TransactionLists.as_view(),  name='Transactins'),
    path('transaction/<int:pk>/', apiviews.TransactionLists.as_view(),  name='Transactins'),
    path("sms/",views.sms, name="sms")

    # can INSERT/CREATE AND SERCAH BY EMAIL OR IMMUNIZATION NAME
    # path('user-by-email-or-phone/', views.UsersList.as_view(), name='user-by-email-or-phone'),
    # path('immunization-by-name/', views.ImmunizationLists.as_view(), name='Users'),
    
]
