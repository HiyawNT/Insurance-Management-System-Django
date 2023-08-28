from django.shortcuts import render, redirect   
from . import forms,models
from manager import models as CMODEL
from customer import models as CustomerModel
from django.contrib.auth.models import User
from django.contrib import messages
import sweetify

# Create your views here.

def payment_dashboard_view(request):
    return render(request, "payment/payment_dashboard.html")



def payments_view(request):
    
        
        
        # transaction_Validator = models.Payment.objects.all().filter(transaction_id__icontains='TD789979TY6FJ')
    PaymentForm=forms.PaymentForm()
    if request.method == 'POST':
        PaymentForm=forms.PaymentForm(request.POST)
        customer = CustomerModel.Customer.objects.get(user_id=request.user.id)
        proof=forms.PaymentForm(request.POST,request.FILES)
        banknameid = request.POST.get('bank_name')
        bankname = models.BankNameLists.objects.get(id=banknameid)               
        categoryid = request.POST.get('payment_type')
        category = models.Category.objects.get(id=categoryid)
        account_no = request.POST.get('account_no')
        Ammount = request.POST.get('payment_amount')       
        userTD = request.POST.get('transaction_id') 
        prOof = request.FILES['payment_proof']
        paymentCommit = PaymentForm.save(commit=False)
        payment_detail = models.Payment(
            customer=customer,
            bank_name= bankname,  category=category,
            account_no = account_no, payment_amount=Ammount, 
            transaction_id = userTD
            
        )
        paymentCommit.bankname = bankname
        paymentCommit.category = category
        paymentCommit.customer = customer
           # paymentCommit.customer = customer
            # paymentCommit.customer = user
        payment_detail.save()
        PaymentForm.payment_proof = prOof
        PaymentForm.save()
        return redirect('verify_payment')
        
    return render(request, 'payment/payment.html', {'PaymentForm':PaymentForm})
    
    
    
                # userTD = request.POST.get('transaction_id')   
            
                # if models.Payment.objects.all().filter(transaction_id=userTD).exists() == True:
                #     print ("IT exists")
                #     return redirect('customer-dashboard')
def payment_history_view(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    payment = models.Payment.objects.all().filter(customer=customer)
    return render(request,'payment/payment_history.html',{'payment':payment,'customer':customer})    






     
def make_payment_view(request):
            # transaction_Validator = models.Payment.objects.all().filter(transaction_id__icontains='TD789979TY6FJ')
    PaymentForm=forms.PaymentForm()

    if request.method == 'POST':
        PaymentForm=forms.PaymentForm(request.POST)
        userTD = request.POST.get('transaction_id') 
        userBA = request.POST.get('account_no')

        if models.Payment.objects.all().filter(transaction_id=userTD).exists():
            if models.Payment.objects.all().filter(account_no=userBA).exists():
                messages.success(request, "Payment Verified")
                return redirect('payment_history')
        else:
            messages.error(request, "Verification Failed  Transaction Id or account Number Wrong  ")
            return redirect('make_payment')
                
                
                
                
           
           
           
            # customer = models.Customer.objects.get(user_id=request.user.id)
            # proof=forms.PaymentForm(request.POST,request.FILES)
            # banknameid = request.POST.get('bank_name')
            # bankname = models.BankNameLists.objects.get(id=banknameid)               
            # categoryid = request.POST.get('payment_type')
            # category = models.Category.objects.get(id=categoryid)
            
            # paymentCommit = proof.save()
            # paymentCommit = PaymentForm.save(commit=False)
            # paymentCommit.bankname = bankname
            # paymentCommit.category = category
            # paymentCommit.customer = customer
           # paymentCommit.customer = customer
            # paymentCommit.customer = user
            # paymentCommit.save()
          
        
    return render(request, 'payment/verify_payment.html', {'PaymentForm':PaymentForm})
      
    
