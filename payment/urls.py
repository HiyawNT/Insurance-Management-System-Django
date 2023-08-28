from django.urls import path
from . import views

urlpatterns = [
    path('verify_payment', views.payments_view, name='verify_payment'),
    
    path('make_payment', views.make_payment_view, name='make_payment'),
    path('payment_dashboard', views.payment_dashboard_view, name='payment_dashboard'),
    path('payment_history', views.payment_history_view, name='payment_history')
]
