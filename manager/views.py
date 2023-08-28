from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from django.db.models import Q
from django.core.mail import send_mail
from django.contrib.auth.models import User
from payment.models import BankNameLists 
from customer import models as CMODEL
from customer import forms as CFORM

def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')  
    return render(request,'frontend/landing-page.html')


def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()

def is_evaluator(user):
    return user.groups.filter(name='EVALUATOR').exists()

# routes actors login 
def afterlogin_view(request):
    if is_customer(request.user):      
        return redirect('customer/customer-dashboard')
    elif is_evaluator(request.user):
        return redirect('evaluator/evaluator-dashboard')
    else:
        return redirect('manager-dashboard')

# def customersignup_view(request):
#    return  render(request, 'customer/customersignup.html')



def managerclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return HttpResponseRedirect('managerlogin')


@login_required(login_url='managerlogin')
def manager_dashboard_view(request):
    dict={
        'total_user':CMODEL.Customer.objects.all().count(),
        'total_policy':models.Policy.objects.all().count(),
        'total_category':models.Category.objects.all().count(),
        'total_question':models.Question.objects.all().count(),
        'total_policy_holder':models.PolicyRecord.objects.all().count(),
        'approved_policy_holder':models.PolicyRecord.objects.all().filter(status='Approved').count(),
        'disapproved_policy_holder':models.PolicyRecord.objects.all().filter(status='Disapproved').count(),
        'waiting_policy_holder':models.PolicyRecord.objects.all().filter(status='Pending').count(),
        'policy_holder_form':models.vehicle_policy.objects.all().count(),
    }
    return render(request,'manager/manager_dashboard.html',context=dict)



@login_required(login_url='stafflogin')
def manager_view_customer_view(request):
    customers= CMODEL.Customer.objects.all()
    return render(request,'manager/manager_view_customer.html',{'customers':customers})



@login_required(login_url='stafflogin')
def update_customer_view(request,pk):
    customer=CMODEL.Customer.objects.get(id=pk)
    user=CMODEL.User.objects.get(id=customer.user_id)
    userForm=CFORM.CustomerUserForm(instance=user)
    customerForm=CFORM.CustomerForm(request.FILES,instance=customer)
    mydict={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        userForm=CFORM.CustomerUserForm(request.POST,instance=user)
        customerForm=CFORM.CustomerForm(request.POST,request.FILES,instance=customer)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customerForm.save()
            return redirect('manager-view-customer')
    return render(request,'manager/update_customer.html',context=mydict)



@login_required(login_url='stafflogin')
def delete_customer_view(request,pk):
    customer=CMODEL.Customer.objects.get(id=pk)
    user=User.objects.get(id=customer.user_id)
    user.delete()
    customer.delete()
    return HttpResponseRedirect('/manager-view-customer')



def manager_category_view(request):
    return render(request,'manager/manager_category.html')

def manager_add_category_view(request):
    categoryForm=forms.CategoryForm() 
    if request.method=='POST':
        categoryForm=forms.CategoryForm(request.POST)
        if categoryForm.is_valid():
            categoryForm.save()
            return redirect('manager-view-category')
    return render(request,'manager/manager_add_category.html',{'categoryForm':categoryForm})

def manager_view_category_view(request):
    categories = models.Category.objects.all()
    return render(request,'manager/manager_view_category.html',{'categories':categories})

def manager_delete_category_view(request):
    categories = models.Category.objects.all()
    return render(request,'manager/manager_delete_category.html',{'categories':categories})
    
def delete_category_view(request,pk):
    category = models.Category.objects.get(id=pk)
    category.delete()
    return redirect('manager-delete-category')

def manager_update_category_view(request):
    categories = models.Category.objects.all()
    return render(request,'manager/manager_update_category.html',{'categories':categories})

@login_required(login_url='managerlogin')
def update_category_view(request,pk):
    category = models.Category.objects.get(id=pk)
    categoryForm=forms.CategoryForm(instance=category)
    
    if request.method=='POST':
        categoryForm=forms.CategoryForm(request.POST,instance=category)
        
        if categoryForm.is_valid():

            categoryForm.save()
            return redirect('manager-update-category')
    return render(request,'manager/update_category.html',{'categoryForm':categoryForm})
  
  

def manager_policy_view(request):
    return render(request,'manager/manager_policy.html')


def manager_add_policy_view(request):
    policyForm=forms.PolicyForm() 
    
    if request.method=='POST':
        policyForm=forms.PolicyForm(request.POST)
        if policyForm.is_valid():
            categoryid = request.POST.get('category')
            category = models.Category.objects.get(id=categoryid)
            
            policy = policyForm.save(commit=False)
            policy.category=category
            policy.save()
            return redirect('manager-view-policy')
    return render(request,'manager/manager_add_policy.html',{'policyForm':policyForm})


def manager_view_policy_view(request):
    policies = models.Policy.objects.all()
    return render(request,'manager/manager_view_policy.html',{'policies':policies})



# CLAIM VIEWS

def manager_claim_view(request):
    return render(request,'manager/manager_claims.html')


def manager_add_claim_view(request):
    claimForm=forms.AddClaimForm() 
    
    if request.method=='POST':
        claimForm=forms.AddClaimForm(request.POST)
        if claimForm.is_valid():
            categoryid = request.POST.get('category')
            category = models.Category.objects.get(id=categoryid)
            
            claim = claimForm.save(commit=False)
            claim.category=category
            claim.save()
            return redirect('manager-view-claim')
    return render(request,'manager/manager_add_claims.html',{'claimForm':claimForm})

def manager_view_claim_view(request):
    claims = models.AddClaim.objects.all()
    return render(request,'manager/manager_view_claim.html',{'claims':claims})




def update_claim_view(request):
    claims = models.AddClaim.objects.all()
    return render(request,'manager/manager_update_claim.html',{'claims':claims})


@login_required(login_url='managerlogin')
def manager_update_claim_view(request,pk):
    claim = models.AddClaim.objects.get(id=pk)
    claimForm=forms.AddClaimForm(instance=claim)
    
    if request.method=='POST':
        claimForm=forms.AddClaimForm(request.POST,instance=claim)
        
        if claimForm.is_valid():

            categoryid = request.POST.get('category')
            category = models.Category.objects.get(id=categoryid)
            
            claim = claimForm.save(commit=False)
            claim.category=category
            claim.save()
           
            return redirect('manager-update-claim')
    return render(request,'manager/update_claims.html',{'claimForm':claimForm})



def manager_delete_claim_view(request):
    claim = models.AddClaim.objects.all()
    return render(request,'manager/manager_delete_claim.html',{'claims':claim})

def delete_claim_view(request,pk):
    claim = models.AddClaim.objects.get(id=pk)
    claim.delete()
    return redirect('manager-delete-claim')















# --------------------------------------------------
def manager_update_policy_view(request):
    policies = models.Policy.objects.all()
    return render(request,'manager/manager_update_policy.html',{'policies':policies})

@login_required(login_url='managerlogin')
def update_policy_view(request,pk):
    policy = models.Policy.objects.get(id=pk)
    policyForm=forms.PolicyForm(instance=policy)
    
    if request.method=='POST':
        policyForm=forms.PolicyForm(request.POST,instance=policy)
        
        if policyForm.is_valid():

            categoryid = request.POST.get('category')
            category = models.Category.objects.get(id=categoryid)
            
            policy = policyForm.save(commit=False)
            policy.category=category
            policy.save()
           
            return redirect('manager-update-policy')
    return render(request,'manager/update_policy.html',{'policyForm':policyForm})


  
  
def manager_delete_policy_view(request):
    policies = models.Policy.objects.all()
    return render(request,'manager/manager_delete_policy.html',{'policies':policies})
    
def delete_policy_view(request,pk):
    policy = models.Policy.objects.get(id=pk)
    policy.delete()
    return redirect('manager-delete-policy')

def manager_view_policy_holder_view(request):
    policyrecords = models.PolicyRecord.objects.all()
    return render(request,'manager/manager_view_policy_holder.html',{'policyrecords':policyrecords})

def manager_view_approved_policy_holder_view(request):
    policyrecords = models.PolicyRecord.objects.all().filter(status='Approved')
    return render(request,'manager/manager_view_approved_policy_holder.html',{'policyrecords':policyrecords})

def manager_view_disapproved_policy_holder_view(request):
    policyrecords = models.PolicyRecord.objects.all().filter(status='Disapproved')
    return render(request,'manager/manager_view_disapproved_policy_holder.html',{'policyrecords':policyrecords})

def manager_view_waiting_policy_holder_view(request):
    policyrecords = models.PolicyRecord.objects.all().filter(status='Pending')
    return render(request,'manager/manager_view_waiting_policy_holder.html',{'policyrecords':policyrecords})


def manager_view_policy_holder_form_view(request):
    vehiclepolicy = models.vehicle_policy.objects.all()
    return render(request,'manager/manager_view_policy_holder_form.html',{'vehiclepolicy':vehiclepolicy})

def approve_request_view(request,pk):
    policyrecords = models.PolicyRecord.objects.get(id=pk)
    policyrecords.status='Approved'
    policyrecords.save()
    return redirect('manager-view-policy-holder')

def disapprove_request_view(request,pk):
    policyrecords = models.PolicyRecord.objects.get(id=pk)
    policyrecords.status='Disapproved'
    policyrecords.save()
    return redirect('manager-view-policy-holder')


def manager_question_view(request):
    questions = models.Question.objects.all()
    return render(request,'manager/manager_question.html',{'questions':questions})

def update_question_view(request,pk):
    question = models.Question.objects.get(id=pk)
    questionForm=forms.QuestionForm(instance=question)
    
    if request.method=='POST':
        questionForm=forms.QuestionForm(request.POST,instance=question)
        
        if questionForm.is_valid():

            manager_comment = request.POST.get('manager_comment')
            
            
            question = questionForm.save(commit=False)
            question.manager_comment=manager_comment
            question.save()
           
            return redirect('manager-question')
    return render(request,'manager/update_question.html',{'questionForm':questionForm})





# custom testing will be deleted when deployed -----start

def loginopt_view(request):
    return render(request, 'frontend/loginopt.html')


def signupopt_view(request):
    return render(request, 'frontend/signupopt.html')

# -----End

def aboutus_view(request):
    return render(request,'frontend/about-us.html')



def productandservices_view(request):
    return render(request,'frontend/product & services.html')

def blog_view(request):
    return render(request,'frontend/blog-grid.html')
def landingpage_view(request):
    banklist1 = BankNameLists(bank_name="COMMERCIAL BANK OF ETHIOPIA")
    banklist2 = BankNameLists(bank_name="ABYSSINIA BANK")
    banklist3 = BankNameLists(bank_name ="WEGEGAN BANK")
    banklist4 = BankNameLists(bank_name="HIBRET BANK")
    banklist5 = BankNameLists(bank_name = "ZEMEN BANK")
    banklists = [banklist1, banklist2, banklist3, banklist4, banklist5]
    if BankNameLists.objects.filter(bank_name = "COMMERCIAL BANK OF ETHIOPIA").exists():
        pass
    else:
        BankNameLists.objects.bulk_create(banklists)

    
    return render(request, 'frontend/landing-page.html')

def contactus_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message,settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, fail_silently = False)
            return render(request, 'manager/contactussuccess.html')
    return render(request, 'frontend/contact-us.html', {'ContactusForm':sub})

