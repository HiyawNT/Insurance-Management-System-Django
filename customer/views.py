from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
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
import secrets


def customerclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'customer/customerclick.html')


def customer_signup_view(request):
    userForm=forms.CustomerUserForm()
    customerForm=forms.CustomerForm()
    mydict={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        userForm=forms.CustomerUserForm(request.POST)
        customerForm=forms.CustomerForm(request.POST,request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customer=customerForm.save(commit=False)
            customer.user=user
            customer.save()
            my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
            my_customer_group[0].user_set.add(user)
        return HttpResponseRedirect('customerlogin')
    return render(request,'customer/customersignup.html',context=mydict)

def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()

@login_required(login_url='customerlogin')
def customer_dashboard_view(request):
    # this is used for the counter or number counting
    dict={
        'customer':models.Customer.objects.get(user_id=request.user.id),
        'available_policy':CMODEL.Policy.objects.all().count(),
        'applied_policy':CMODEL.PolicyRecord.objects.all().filter(customer=models.Customer.objects.get(user_id=request.user.id)).count(),
        'claim_form':CMODEL.AddClaim.objects.all().count(),
        'total_question':CMODEL.Question.objects.all().filter(customer=models.Customer.objects.get(user_id=request.user.id)).count(),

    }
    return render(request,'customer/customer_dashboard.html',context=dict)


@login_required(login_url='customerlogin')
def view_profile_view(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    return render(request,'customer/view_customer_profile.html',{'Customer':customer})


@login_required(login_url='customerlogin')
def update_customer_view(request,pk):
    customer=models.Customer.objects.get(id=pk)
    user=CMODEL.User.objects.get(id=customer.user_id)
    userForm=forms.CustomerUserForm(instance=user)
    customerForm=forms.CustomerForm(request.FILES,instance=customer)
    mydict={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        userForm=forms.CustomerUserForm(request.POST,instance=user)
        customerForm=forms.CustomerForm(request.POST,request.FILES,instance=customer)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customerForm.save()
            return redirect('view-profile')
    return render(request,'customer/update_profile.html',context=mydict)






def apply_policy_view(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    policies = CMODEL.Policy.objects.all()
    return render(request,'customer/apply_policy.html',{'policies':policies,'customer':customer})



def apply_claim_form(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    claims = CMODEL.vehicle_policy.objects.all()
    return render(request,'customer/apply_claims.html',{'claims':claims,'customer':customer})


# --------------------------------------------------------------------------------------------


def claim_form_view(request, pk):
    claimform = forms.ClaimForm()
    
    if request.method == 'POST':
        claimform=forms.ClaimForm(request.POST)

        customer = models.Customer.objects.get(user_id=request.user.id)
        insured_name = request.POST.get('insured_name')
        phone_no = request.POST.get('phone_no')
        address = request.POST.get('address')
        profession = request.POST.get('profession')
        policy_number = request.POST.get('policy_number')
        renewal_date = request.POST.get('renewal_date')
        vehiclemodel = request.POST.get('vehiclemodel')
        yearofmanufacture = request.POST.get('yearofmanufacture')
        plateno = request.POST.get('plateno')
        licenceno = request.POST.get('licenceno')
        vehicle_purpose = request.POST.get('vehicle_purpose')
        horsepower = request.POST.get('horsepower')
        carrying_capacity = request.POST.get('carrying_capacity')
        driver_name = request.POST.get('driver_name')
        driver_age = request.POST.get('driver_age')
        driver_phone_no = request.POST.get('driver_phone_no')
        licence_expiry_date = request.POST.get('licence_expiry_date')
        driver_address = request.POST.get('driver_address')
        licence_number = request.POST.get('licence_number')
        driver_profession = request.POST.get('driver_profession')
        licence_grade = request.POST.get('licence_grade')
        accident_proof = request.POST.get('accident_proof')
        accident_date = request.POST.get('accident_date')
        accident_place = request.POST.get('accident_place')
        accident_time = request.POST.get('accident_time')
        accident_description = request.POST.get('accident_description')
        ClaimFormCommit = CMODEL.claim_form(
                customer = customer,
                insured_name = insured_name, phone_no = phone_no, address = address, profession = profession,
                policy_number = policy_number, renewal_date = renewal_date, vehiclemodel = vehiclemodel, yearofmanufacture = yearofmanufacture,
                plateno = plateno, licenceno = licenceno, vehicle_purpose = vehicle_purpose, horsepower = horsepower, carrying_capacity = carrying_capacity,
                driver_name = driver_name, driver_age = driver_age, driver_phone_no = driver_phone_no, licence_expiry_date = licence_expiry_date,
                driver_address = driver_address, licence_number = licence_number, driver_profession = driver_profession, licence_grade = licence_grade,
                accident_proof = accident_proof, accident_date = accident_date, accident_place = accident_place, accident_time = accident_time, accident_description = accident_description
                
            )
        ClaimFormCommit.save()
        claim = CMODEL.apply_claims .objects.get(id=pk)
        policyrecord = CMODEL.ClaimRecord()
        policyrecord.claim = claim
        policyrecord.customer = customer
        policyrecord.save()
        return redirect('history')
        # return redirect('customer-dashboard')
            
        
    return render(request, 'customer/claim_form.html', {'ClaimForm' : claimform} )
 
 
 
def claim_translated_form_view(request):
    claimform = forms.ClaimForm()
    return render(request, 'customer/claim_translated.html', {'ClaimForm' : claimform})
    


def apply_view(request,pk):
    customer = models.Customer.objects.get(user_id=request.user.id)
    policy = CMODEL.Policy.objects.get(id=pk)
    policyrecord = CMODEL.PolicyRecord()
    policyrecord.Policy = policy
    policyrecord.customer = customer
    policyrecord.save()
    return redirect('history')

def payments_view(request):
        PaymentForm=forms.PaymentForm(request.POST)
        if PaymentForm.is_valid():
            banknameid = request.POST.get('bank_name')
            bankname = models.BankNameLists.objects.get(name=banknameid)
            
            paymentCommit = PaymentForm.save(commit=False)
            paymentCommit.bankname = bankname
            paymentCommit.save()
        return render(request, 'customer/payment.html', {'PaymentForm':PaymentForm})
    
@csrf_exempt
def policy_form_view(request, pk):
    policyform = forms.PolicyForm()
    if request.method == 'POST':
        policyform=forms.PolicyForm(request.POST)
        
        customer = models.Customer.objects.get(user_id=request.user.id)
        policy_number = secrets.token_hex(5)
        proposer_name = request.POST.get('proposer_name')
        father_name = request.POST.get('father_name')
        age = request.POST.get('age')
        address = request.POST.get('address')
        profession = request.POST.get('profession')
        phone_no = request.POST.get('phone_no')
        pobox = request.POST.get('pobox')
      
        licenceno = request.POST.get('licenceno')
        durationfrom = request.POST.get('durationfrom')
        durationto = request.POST.get('durationto')
        policychoice = request.POST.get('policychoice')
        plateno = request.POST.get('plateno')
        vehiclename = request.POST.get('vehiclename')
        vehiclemodel = request.POST.get('vehiclemodel')
        yearofmanufacture = request.POST.get('yearofmanufacture')
        yearofpurchase = request.POST.get('yearofpurchase')
        priceofcar = request.POST.get('priceofcar')
        policyformCommit = CMODEL.vehicle_policy(
                customer = customer,
                policy_number = policy_number,
                proposer_name = proposer_name, father_name = father_name, age = age,
                address = address, profession = profession, phone_no = phone_no,
                pobox = pobox, policychoice = policychoice, licenceno = licenceno,
                durationfrom = durationfrom, durationto = durationto, plateno = plateno, 
                vehiclename = vehiclename, vehiclemodel = vehiclemodel, yearofmanufacture = yearofmanufacture,
                yearofpurchase = yearofpurchase, priceofcar = priceofcar 
            )
        
        
        policyformCommit.save()
        policy = CMODEL.Policy.objects.get(id=pk)
        policyrecord = CMODEL.PolicyRecord()
        policyrecord.Policy = policy
        policyrecord.customer = customer
        policyrecord.save()
        return redirect('history')
    else:
        return render(request, 'customer/vehicle-policy.html', {'PolicyForm' : policyform})






def history_view(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    policies = CMODEL.PolicyRecord.objects.all().filter(customer=customer)
    return render(request,'customer/history.html',{'policies':policies,'customer':customer})

def ask_question_view(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    questionForm=CFORM.QuestionForm() 
    
    if request.method=='POST':
        questionForm=CFORM.QuestionForm(request.POST)
        if questionForm.is_valid():
            
            question = questionForm.save(commit=False)
            question.customer=customer
            question.save()
            return redirect('question-history')
    return render(request,'customer/ask_question.html',{'questionForm':questionForm,'customer':customer})

def question_history_view(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    questions = CMODEL.Question.objects.all().filter(customer=customer)
    return render(request,'customer/question_history.html',{'questions':questions,'customer':customer})

