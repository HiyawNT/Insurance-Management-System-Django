from django.db import models
from customer.models import Customer
# to import the Catagory class from manager/models
from manager.models import Category

# Payment Models


class BankNameLists(models.Model):
    bank_name = models.CharField(max_length=40)
    def __str__(self):
        return self.bank_name
# payment type is foreign key so fix that
   
class Payment(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    bank_name = models.ForeignKey(BankNameLists, on_delete=models.CASCADE)
    category= models.ForeignKey(Category, on_delete=models.CASCADE) 
    # payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    account_no = models.BigIntegerField()
    payment_amount = models.PositiveIntegerField(null=True)
    transaction_id = models.CharField(max_length=60)
    payment_proof = models.ImageField(upload_to='payments/receipts/',null=True,blank=True)   
    payed_date =models.DateField(auto_now=True)
