from django.urls import path
from accounts import views

urlpatterns = [

    # GET and POST
    path('users/', views.UserView.as_view(),  name='Users'),
    # GET, PUT, DELETE
    path('users/<int:pk>/', views.UserDetail.as_view(),  name='Users'),
    path('nok/', views.NOKLists.as_view(),  name='Users'),
    path('account/', views.AccountLists.as_view(),  name='Account'),
    path('transaction/', views.TransactionLists.as_view(),  name='Transactins'),
    path('transaction/<int:pk>/', views.TransactionLists.as_view(),  name='Transactins'),

    # can INSERT/CREATE AND SERCAH BY EMAIL OR IMMUNIZATION NAME
    # path('user-by-email-or-phone/', views.UsersList.as_view(), name='user-by-email-or-phone'),
    # path('immunization-by-name/', views.ImmunizationLists.as_view(), name='Users'),
    
]
