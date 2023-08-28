from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('evaluatorsignup', views.Evaluator_signup_view,name='evaluatorsignup'),
    path('evaluator-dashboard', views.evaluator_dashboard_view,name='evaluator-dashboard'),
    path('evaluatorlogin', LoginView.as_view(template_name='manager/stafflogin.html'),name='evaluatorlogin'),
    path('update-profile/<int:pk>', views.update_profile_view,name='update-profile'),
    path('view-profile', views.view_profile_view,name='view-profile'),
    
    

]
