from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('customerclick', views.customerclick_view,name='customerclick'),
    path('customersignup', views.customer_signup_view,name='customersignup'),
    path('customer-dashboard', views.customer_dashboard_view,name='customer-dashboard'),
    path('customerlogin', LoginView.as_view(template_name='manager/stafflogin.html'),name='customerlogin'),
    path('view-profile', views.view_profile_view,name='view-profile'),
    path('update-profile/<int:pk>', views.update_customer_view,name='update-profile'),
    path('policy-form/<int:pk>', views.policy_form_view, name='policy-form'),
    path('apply_claims', views.apply_claim_form, name = 'apply_claims'),
    path('claim_form/<int:pk>', views.claim_form_view, name='claim_form'),
    path('claim_translated/', views.claim_translated_form_view, name='claim_translated'),

    path('apply-policy', views.apply_policy_view,name='apply-policy'),
    path('payments', views.payments_view, name='payments'),
    path('apply/<int:pk>', views.apply_view,name='apply'),
    path('history', views.history_view,name='history'),

    path('ask-question', views.ask_question_view,name='ask-question'),
    path('question-history', views.question_history_view,name='question-history'),
]