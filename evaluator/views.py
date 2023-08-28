from django.shortcuts import render
from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group, User
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from django.db.models import Q
from django.core.mail import send_mail
from manager import models as CMODEL
from manager import forms as CFORM
from django.contrib.auth.models import User
# Create your views here.

def Evaluator_signup_view(request):
    EvaluatorUserForm=forms.EvaluatorUserForm()
    EvaluatorForm=forms.EvaluatorForm()
    mydict={'EvaluatorUserForm':EvaluatorUserForm,'EvaluatorForm':EvaluatorForm}
    if request.method=='POST':
        EvaluatorUserForm=forms.EvaluatorUserForm(request.POST)
        EvaluatorForm=forms.EvaluatorForm(request.POST,request.FILES)
        if EvaluatorUserForm.is_valid() and EvaluatorForm.is_valid():
            user=EvaluatorUserForm.save()
            user.set_password(user.password)
            user.save()
            evaluator=EvaluatorForm.save(commit=False)
            evaluator.user=user
            evaluator.save()
            my_evaluator_group = Group.objects.get_or_create(name='EVALUATOR')
            my_evaluator_group[0].user_set.add(user)
        return HttpResponseRedirect('evaluatorlogin')
    return render(request,'Evaluator/evaluatorsignup.html',context=mydict)
def is_evaluator(user):
    return user.groups.filter(name='EVALUATOR').exists()

@login_required(login_url='evaluatorlogin')
def evaluator_dashboard_view(request):
    dict={
        'Evaluator':models.Evaluator.objects.get(user_id=request.user.id),
        # 'available_policy':CMODEL.Policy.objects.all().count(),
        # 'applied_policy':CMODEL.PolicyRecord.objects.all().filter(customer=models.Customer.objects.get(user_id=request.user.id)).count(),
        # 'total_category':CMODEL.Category.objects.all().count(),
        # 'total_question':CMODEL.Question.objects.all().filter(customer=models.Customer.objects.get(user_id=request.user.id)).count(),

    }
    return render(request,'Evaluator/evaluator_dashboard.html',context=dict)



@login_required(login_url='evaluatorlogin')
def view_profile_view(request):
    evaluator = models.Evaluator.objects.get(user_id=request.user.id)
    return render(request,'Evaluator/view_profile.html',{'Evaluator':evaluator})


@login_required(login_url='evaluatorlogin')
def update_profile_view(request,pk):
    evaluator=models.Evaluator.objects.get(id=pk)
    user=CMODEL.User.objects.get(id=evaluator.user_id)
    userForm=forms.EvaluatorUserForm(instance=user)
    evaluatorForm=forms.EvaluatorForm(request.FILES,instance=evaluator)
    mydict={'userForm':userForm,'evaluatorForm':evaluatorForm}
    if request.method=='POST':
        userForm=forms.EvaluatorUserForm(request.POST,instance=user)
        evaluatorForm=forms.EvaluatorForm(request.POST,request.FILES,instance=evaluator)
        if userForm.is_valid() and evaluatorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            evaluatorForm.save()
            return redirect('evaluator-dashboard')
    return render(request,'Evaluator/update_profile.html',context=mydict)