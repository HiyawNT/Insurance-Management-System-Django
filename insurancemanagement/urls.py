
from django.contrib import admin
from django.urls import path
from manager import views
from django.contrib.auth.views import LogoutView,LoginView
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),


    path('customer/',include('customer.urls')),
    path('payment/',include('payment.urls')),
    path('evaluator/',include('evaluator.urls')),
    path('',views.home_view,name='landing-page'),
    # path('index', views.index_view, name='index'),
    path('loginopt', views.loginopt_view, name='loginopt'),
    path('signupopt', views.signupopt_view, name='signupopt'),
    path('landing-page', views.landingpage_view, name='landing-page'),
    path('logout', LogoutView.as_view(template_name='manager/logout.html'),name='logout'),
    path('about-us', views.aboutus_view),
    path('contact-us', views.contactus_view),
    path('product&services', views.productandservices_view),
    path('blog', views.blog_view),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),

    
    # path('customersignup', views.customersignup_view, name='customersignup'),
    path('customerlogin', LoginView.as_view(template_name='manager/stafflogin.html'),name='customerlogin'),
    path('stafflogin', LoginView.as_view(template_name='manager/stafflogin.html'),name='stafflogin'),
    path('evaluatorlogin', LoginView.as_view(template_name='manager/stafflogin.html'),name='evaluatorlogin'),
    
    
    path('manager-dashboard', views.manager_dashboard_view,name='manager-dashboard'),

    path('manager-view-customer', views.manager_view_customer_view,name='manager-view-customer'),
    path('update-customer/<int:pk>', views.update_customer_view,name='update-customer'),
    path('delete-customer/<int:pk>', views.delete_customer_view,name='delete-customer'),

    path('manager-category', views.manager_category_view,name='manager-category'),
    path('manager-view-category', views.manager_view_category_view,name='manager-view-category'),
    path('manager-update-category', views.manager_update_category_view,name='manager-update-category'),
    path('update-category/<int:pk>', views.update_category_view,name='update-category'),
    path('manager-add-category', views.manager_add_category_view,name='manager-add-category'),
    path('manager-delete-category', views.manager_delete_category_view,name='manager-delete-category'),
    path('delete-category/<int:pk>', views.delete_category_view,name='delete-category'),


    path('manager-policy', views.manager_policy_view,name='manager-policy'),
    path('manager-add-policy', views.manager_add_policy_view,name='manager-add-policy'),
    path('manager-view-policy', views.manager_view_policy_view,name='manager-view-policy'),
    path('manager-update-policy', views.manager_update_policy_view,name='manager-update-policy'),
    path('update-policy/<int:pk>', views.update_policy_view,name='update-policy'),
    path('manager-delete-policy', views.manager_delete_policy_view,name='manager-delete-policy'),
    path('delete-policy/<int:pk>', views.delete_policy_view,name='delete-policy'),

    
    
    path('manager-claim', views.manager_claim_view,name='manager-claim'),
    path('manager-add-claim', views.manager_add_claim_view,name='manager-add-claim'),
    path('manager-view-claim', views.manager_view_claim_view,name='manager-view-claim'),
    path('manager-update-claim', views.update_claim_view,name='manager-update-claim'),
    path('update-claim/<int:pk>', views.manager_update_claim_view,name='update-claim'),
    path('manager-delete-claim', views.manager_delete_claim_view,name='manager-delete-claim'),
    path('delete-claim/<int:pk>', views.delete_claim_view,name='delete-claim'),
    
    
    
    path('manager-view-policy-holder', views.manager_view_policy_holder_view,name='manager-view-policy-holder'),
    path('manager-view-approved-policy-holder', views.manager_view_approved_policy_holder_view,name='manager-view-approved-policy-holder'),
    path('manager-view-disapproved-policy-holder', views.manager_view_disapproved_policy_holder_view,name='manager-view-disapproved-policy-holder'),
    path('manager-view-waiting-policy-holder', views.manager_view_waiting_policy_holder_view,name='manager-view-waiting-policy-holder'),
    path('manager-view-policy-holder-form', views.manager_view_policy_holder_form_view,name='manager-view-policy-holder-form'),
    path('approve-request/<int:pk>', views.approve_request_view,name='approve-request'),
    path('reject-request/<int:pk>', views.disapprove_request_view,name='reject-request'),

    path('manager-question', views.manager_question_view,name='manager-question'),
    path('update-question/<int:pk>', views.update_question_view,name='update-question'),

]
