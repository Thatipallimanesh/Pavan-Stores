from django.urls import path
from useraccounts import views

urlpatterns=[
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
]