from django.db import models
from django.contrib.auth.models import User
from customer.models import Customer
class Category(models.Model):
    category_name =models.CharField(max_length=20)
    creation_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.category_name

class Policy(models.Model):
    category= models.ForeignKey('Category', on_delete=models.CASCADE)
    policy_name=models.CharField(max_length=200)
    sum_assurance=models.PositiveIntegerField()
    premium=models.PositiveIntegerField()
    tenure=models.PositiveIntegerField()
    creation_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.policy_name

class PolicyRecord(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    Policy= models.ForeignKey(Policy, on_delete=models.CASCADE)
    status = models.CharField(max_length=100,default='Pending')
    creation_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.Policy

class Question(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    description =models.CharField(max_length=500)
    manager_comment=models.CharField(max_length=200,default='Nothing')
    asked_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.description
class vehicle_policy_type:
    vehicle_policy =models.CharField(max_length=20)
    def __str__(self):
        return self.vehicle_policy
    
# claim Type

class claim_type(models.Model):
    ClaimType = models.CharField(max_length=20)
    def __str__(self):
        return self.ClaimType
    
class AddClaim(models.Model):
    category= models.ForeignKey('Category', on_delete=models.CASCADE)
    claim_name=models.CharField(max_length=200)
    creation_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.claim_name
    
Policy_Choice= [
    ('Comprehensive', 'Comprehensive '),
    ('Third Party only', 'Third Party only'),
    ('Third Party, Fire and Theft', 'Third Party, Fire and Theft'),
    ]

class vehicle_policy(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    policy_number = models.CharField(max_length=15)
    creation_date =models.DateField(auto_now=True)
    proposer_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=50)
    profession = models.CharField(max_length=80)
    phone_no = models.BigIntegerField()
    pobox = models.PositiveIntegerField()
    policychoice = models.CharField(max_length=40, choices=Policy_Choice, default='Comprehensive')
    licenceno = models.PositiveIntegerField()
    durationfrom = models.CharField(max_length=50)
    durationto = models.CharField(max_length=50)
    plateno = models.CharField(max_length=10)
    vehiclename = models.CharField(max_length=50)
    vehiclemodel = models.CharField(max_length=50)
    yearofmanufacture = models.CharField(max_length=50)
    yearofpurchase =  models.CharField(max_length=50)
    priceofcar = models.CharField(max_length=50)
    def __str__(self):
        return self.proposer_name
  
    # claims ------------------------------------
    #  related name must be diffrent for the reverse accessor to work
# class apply_claims(models.Model):
#     customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
#     type = models.ForeignKey(claim_type, on_delete=models.CASCADE, default='')
#     policy_number = models.ForeignKey(vehicle_policy, related_name='Policy_number', on_delete=models.CASCADE)
#     creation_date = models.ForeignKey(vehicle_policy,related_name='Creation_date', on_delete=models.CASCADE)
#     vehiclename = models.ForeignKey(vehicle_policy, related_name='Vehiclename', on_delete=models.CASCADE)
#     vehiclemodel = models.ForeignKey(vehicle_policy, related_name='Vehiclemodel', on_delete=models.CASCADE)
#     durationfrom = models.ForeignKey(vehicle_policy, related_name='Durationfrom', on_delete=models.CASCADE)
#     durationto = models.ForeignKey(vehicle_policy,related_name='Durationto', on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.policy_number 
        
# class ClaimRecord(models.Model):
#     customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
#     claim= models.ForeignKey(apply_claims, on_delete=models.CASCADE)
#     status = models.CharField(max_length=100, default='Pending')
#     creation_date =models.DateField(auto_now=True)
#     def __str__(self):
#         return self.claim

class claim_form(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    policy_type = models.ForeignKey('Category', on_delete=models.CASCADE)
    policy_number = models.ForeignKey(vehicle_policy, on_delete=models.CASCADE)
    creation_date =models.DateField(auto_now=True)
    insured_name = models.CharField(max_length=50)
    phone_no = models.PositiveIntegerField()
    address = models.CharField(max_length=50)
    profession = models.CharField(max_length=80)
    renewal_date= models.DateField()
    
 # Vehicle Information Table
 
    vehiclemodel = models.CharField(max_length=50)
    yearofmanufacture = models.CharField(max_length=50)
    plateno = models.CharField(max_length=10)
    licenceno = models.PositiveIntegerField()
    vehicle_purpose = models.CharField(max_length=50)
    horsepower = models.CharField(max_length=50)
    carrying_capacity = models.CharField(max_length=50)
# Driver's Information Table  
    driver_name = models.CharField(max_length=50)
    driver_age = models.PositiveIntegerField()
    driver_phone_no = models.PositiveIntegerField()
    driver_address = models.CharField(max_length=50)
    licence_number = models.CharField(max_length=50)
    driver_profession = models.CharField(max_length=80)
    licence_grade =  models.PositiveIntegerField()
    licence_expiry_date = models.DateField()
    accident_date = models.DateField()
    accident_time = models.CharField(max_length=10)
    accident_place = models.CharField(max_length=40)
    accident_description = models.CharField(max_length=500)
    
    accident_proof= models.ImageField(upload_to='accident_pic/',null=True,blank=True)
    def __str__(self):
        return self.vehicle_policy
    
    
    
class Contactus(models.Model):
    Name = models.CharField(max_length=30)
    Subject = models.CharField(max_length=70)
    Email = models.EmailField()
    Message = models.CharField(max_length=500)
    
    def __str__(self):
        return self.Name
    