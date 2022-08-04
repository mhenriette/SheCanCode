from django.urls import path
from . import views

urlpatterns = [
 
     path('', views.home, name='home'),
     path('signup/', views.signup, name='signup'),
     path('account/', views.account, name='account'),
     path('sendmoney/',views.sendmoney, name='sendmoney')
]
