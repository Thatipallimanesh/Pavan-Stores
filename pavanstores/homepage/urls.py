from django.urls import path
from homepage import views

urlpatterns = [
    path('', views.index, name="index"),
    # whenever http://127.0.0.1:8000/ is opened, call index function from views.py
    path('checkout', views.checkout, name="checkout"),
    path('orderTracker', views.orderTracker, name="orderTracker"),
    path('orderCancellation', views.cancel, name="cancel"),
    path('confirmCancellation', views.confirm, name="confirm"),
]
