from abc import ABC, abstractmethod
import random
import json
import uuid
from datetime import datetime
#-----------------------------------------------------User define Modules------------------
from sendverifymessage import client_notification_message,admin_verificaton_message
from viewpaymentlist_module import viewAllpaymentList
from BankTransfer import DomesticBankTransfer,InternationalBankTransfer
#payment lists-----------------------------------------------
creditcardpayment_list=[]
paypalpayment_list=[]
cashpayment_list=[]
cryptopayment_list=[]
# admins log in list--------------------------------------------
admin_list=[]
# Bank transfer list-------------------------------------------
domestic_bank=[]
# international transfer list---------------------------------
international_bank=[]

#login and signup list----------------------------------------
login_list=[]
singup_list=[]
#payment files-----------------------------------------------
creditcardpayment_file="data/creditcardpayment.json"
paypalpayment_file="data/paypalpayment.json"
cashpayment_file="data/cashpayment.json"
cryptopayment_file="data/cryptopayment.json"
admin_file="data/adminInfo.json"
domestic_bank_file="data/domestic_Bank_Transfer.json"
signUp_file="data/signup_list.json"
class paymentProcessingSystem(ABC):
    @abstractmethod
    def process_payment(self,amount):
        pass
    @abstractmethod
    def get_receipt(self):
        pass

class CreditCardPayment(paymentProcessingSystem):
    def __init__(self,card_number,card_holder_name,expriy_date,cvv,phone,transcation_ID):
        self.card_number=card_number
        self.card_holder_name=card_holder_name
        self.expriy_date=expriy_date
        self.cvv=cvv
        self.transcation_ID=transcation_ID
        self.phone=phone
    def process_payment(self, amount):
        print(f"Processing Credit Card pyamentof TK.{amount} for {self.card_holder_name}")
    def get_receipt(self):
        return f"Receipt Credit Card ending in {self.card_number[-4:]}"
    def save_creditcardpayment(self,amount):
        creditcardpayment_list.append({
            "card_number":self.card_number,
            "card_holder_name":self.card_holder_name,
            "expriy_date":self.expriy_date,
            "cvv":self.cvv,
            "amount":amount,
            "phone":self.phone,
            "transcation_ID":self.transcation_ID,
            "date_time":datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        })
        with open(creditcardpayment_file,"w") as f:
            json.dump(creditcardpayment_list,f,indent=4)
    def view_creditcard_payment(self):
        print(f"{"*"*50} Credit Card Payment {"*"*50}")
        with open(creditcardpayment_file,"r") as f:
            data=json.load(f)
            for i in data:
                print(i)
    def gobackTranscation_ID(self):
        return self.transcation_ID

class PayPalPayment(paymentProcessingSystem):
    def __init__(self,name,email,password,phone,transcation_ID):
        self.name=name
        self.email=email
        self.password=password
        self.phone=phone
        self.transcation_ID=transcation_ID
    def process_payment(self, amount):
        print(f"Processing PayPal Payment of TK.{amount} for {self.email}")
    def get_receipt(self):
        return f"Receipt: PayPal transaction for {self.email}"
    def save_paypalpayment(self,amount):
        paypalpayment_list.append({
            "name":self.name,
            "email":self.email,
            "password":self.password,
            "amount":amount,
            "phone":self.phone,
            "transcation_ID":self.transcation_ID,
            "date_time":datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        })
        with open(paypalpayment_file,"w") as f:
            json.dump(paypalpayment_list,f,indent=4)
    def view_paypal_payment(self):
        print(f"{"*"*50} PayPal Payment {"*"*50}")
        with open(paypalpayment_file,"r") as f:
            data=json.load(f)
            for i in data:
                print(i)
    def gobackTranscation_ID(self):
        return self.transcation_ID

class CashPayment(paymentProcessingSystem):
    def __init__(self,name,phone,transcation_ID):
        self.name=name
        self.phone=phone
        self.transcation_ID=transcation_ID
    def process_payment(self,amount):
        print(f"Processing Cash Payment of TK.{amount} for {self.name}")
    def get_receipt(self):
        return f"Receipt: Cash payment for {self.name}"
    def save_cashpayment(self,amount):
        cashpayment_list.append({
            "name":self.name,
            "phone":self.phone,
            "amount":amount,
            "transcation_ID":self.transcation_ID,
            "date_time":datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        })
        with open(cashpayment_file,"w") as f:
            json.dump(cashpayment_list,f,indent=4)
    def view_cash_payment(self):
        print(f"{"*"*50} Cash Payment {"*"*50}")
        with open(cashpayment_file,"r") as f:
            data=json.load(f)
            for i in data:
                print(i)
    def gobackTranscation_ID(self):
        return self.transcation_ID

class CryptoPayment(paymentProcessingSystem):
    def __init__(self,email,crypto_id,phone,transcation_ID):
        self.email=email
        self.crypto_id=crypto_id
        self.phone=phone
        self.transcation_ID=transcation_ID
    def process_payment(self, amount):
        print(f'processing Crypto Payment of TK.{amount} for {self.email}')
    def get_receipt(self):
        return f"Receipt: Crypto payment for {self.email}"
    def save_cryptopayment(self,amount):
        cryptopayment_list.append({
            "email":self.email,
            "crypto_id":self.crypto_id,
            "amount":amount,
            "phone":self.phone,
            "transcation_ID":self.transcation_ID,
            "date_time":datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        })
        with open(cryptopayment_file,"w") as f:
            json.dump(cryptopayment_list,f,indent=4)
    def view_crypto_payment(self):
        print(f"{"*"*50} Crypto Payment {"*"*50}")
        with open(cryptopayment_file,"r") as f:
            data=json.load(f)
            for i in data:
                print(i)
    def gobackTranscation_ID(self):
        return self.transcation_ID

#make payment---------------------------------------------------------------------------------
def make_payment(paymentProcessor,amount):
    paymentProcessor.process_payment(amount)
    print(paymentProcessor.get_receipt())

#restore data-----------------------------------------------------------------------------------
def restore_data(creditcardpayment,paypalypayment,cashpayment,cryptopayment,adminlist,domesticBanklist,singupList):
    with open(creditcardpayment_file,"r") as f:
        creditcardpayment=json.load(f)
    with open(paypalpayment_file,"r") as f:
        paypalypayment=json.load(f)
    with open(cashpayment_file,"r") as f:
        cashpayment=json.load(f)
    with open(cryptopayment_file,"r") as f:
        cryptopayment=json.load(f)
    with open(admin_file,"r") as f:
        adminlist=json.load(f)
    with open(domestic_bank_file,"r") as f:
        domesticBanklist=json.load(f)
    with open(signUp_file,"r") as f:
        singupList=json.load(f)
    return creditcardpayment,paypalypayment,cashpayment,cryptopayment,adminlist,domesticBanklist,singupList

#save data***********************************************


#-admin part=================================================================
def adminFunction():
    name=input("Enter yourr name: ")
    email=input("Enter your email: ")
    phone=input("Enter your phone: ")
    admin_id=input("Enter your ID: ")
    admin_list.append({
        "admin_id":admin_id+str(random.randint(452,897)),
        "name":name,
        "email":email,
        "phone":phone
    })
    with open(admin_file,'w') as f:
        json.dump(admin_list,f,indent=4)




if __name__=="__main__":
    creditcardpayment_list,paypalpayment_list,cashpayment_list,cryptopayment_list,admin_list,domestic_bank,singup_list=restore_data(creditcardpayment_list,paypalpayment_list,cashpayment_list,cryptopayment_list,admin_list,domestic_bank,singup_list)
    print(f"{'-'*50} Payment Processing System {'-'*50}")
    print("1.Long In         2.Sign Up")
    option=input("Enter Your Choice: ")
    match option:
        case '1':
            log_email=input("Enter Your Email address: ")
            log_password=input("Enter your Password: ")
            for data in singup_list:
                if(log_email in data['email'] and log_password in data['password']):
                    print("**************** Log In successfully Completed *******************")
                    while True:            
                        print(f"{'-'*50} Payment Processing System {'-'*50}"
                            "\n 1. Credit Card Payment       a. view Credit Card Payment"
                            "\n 2. PayPal Payment            b. view PayPal Payment"
                            "\n 3. Cash Payment              c. view Cash Payment"
                            "\n 4. Crypto Payment            d. view Crypto Payment"
                            "\n 0. Exit                      e. Admin Registration"
                            "\n f. Domestic Bank Transfer")
                        option=input("Enter you payment option: ")
                        match option:
                            case '1':
                                card_number=input("Enter Card Number (12 digit): ")
                                card_holder_name=input("Enter Card Holder Name: ")
                                expriy_date=input("Enter expiry date (Mounth/Year): ")
                                cvv=input('Enter CVV : ')
                                phone=input("Enter your phone number(start with +880-) : ")
                                payment_value=int(input("Enter payment amount: "))
                                transcation=str(uuid.uuid4())
                                cc_payment=CreditCardPayment(card_number,card_holder_name,expriy_date,cvv,phone,transcation)
                                make_payment(cc_payment,payment_value)
                                cc_payment.save_creditcardpayment(payment_value)
                                transcation_id=cc_payment.gobackTranscation_ID()
                                admin_verificaton_message(0,transcation_id,payment_value,phone)
                                client_notification_message(0,transcation_id,payment_value,phone)
                            case '2':
                                name=input("Enter name: ")
                                email=input("Enter email: ")
                                password=input("Enter password: ")
                                phone=input("Enter your phone number(start with +880-) : ")
                                payment_value=int(input("Enter payment amount: "))
                                transcation=str(uuid.uuid4())
                                pp_payment=PayPalPayment(name,email,password,phone,transcation)
                                make_payment(pp_payment,payment_value)
                                pp_payment.save_paypalpayment(payment_value)
                                transcation_id=pp_payment.gobackTranscation_ID()
                                admin_verificaton_message(1,transcation_id,payment_value,phone)
                                client_notification_message(1,transcation_id,payment_value,phone)
                            case '3':
                                name=input("Enter name: ")
                                phone=input("Enter phone number: ")
                                payment_value=int(input("Enter payment amount: "))
                                transcation=str(uuid.uuid4())
                                cash_payment=CashPayment(name,phone,transcation)
                                make_payment(cash_payment,payment_value)
                                cash_payment.save_cashpayment(payment_value)
                                transcation_id=cash_payment.gobackTranscation_ID()
                                admin_verificaton_message(2,transcation_id,payment_value,phone)
                                client_notification_message(2,transcation_id,payment_value,phone)
                            case '4':
                                email=input("Enter email: ")
                                crypto_id=input("Enter crypto id: ")
                                phone=input("Enter your phone number(start with +880-) : ")
                                payment_value=int(input("Enter payment amount: "))
                                transcation=str(uuid.uuid4())
                                crypto_payment=CryptoPayment(email,crypto_id,phone,transcation)
                                make_payment(crypto_payment,payment_value)
                                crypto_payment.save_cryptopayment(payment_value)
                                transcation_id=crypto_payment.gobackTranscation_ID()
                                admin_verificaton_message(3,transcation_id,payment_value,phone)
                                client_notification_message(3,transcation_id,payment_value,phone)
                            case 'a':
                                viewAllpaymentList('a',admin_file)
                                #------------------------------------if all argument are match to peramerter than use this code----------------------------
                                # cc_payment=[CreditCardPayment(**creditcard) for creditcard in creditcardpayment_list]
                                # for cc in cc_payment:
                                #     cc.view_creditcard_payment()
                            case 'b':
                                viewAllpaymentList('b',admin_file)
                                #------------------------------------if all argument are match to peramerter than use this code----------------------------
                                # pp_payment=[PayPalPayment(**paypal) for paypal in paypalpayment_list]
                                # for pp in pp_payment:
                                #     pp.view_paypal_payment()
                            case 'c':
                                viewAllpaymentList('c',admin_file)
                                #------------------------------------if all argument are match to peramerter than use this code----------------------------
                                # cash_payment=[CashPayment(**cash) for cash in cashpayment_list]
                                # for cash in cash_payment:
                                #     cash.view_cash_payment() 
                            case 'd':
                                viewAllpaymentList('d',admin_file)
                                #------------------------------------if all argument are match to peramerter than use this code----------------------------
                                # crypto_payment=[CryptoPayment(**crypto) for crypto in cryptopayment_list]
                                # for crypto in crypto_payment:
                                #     crypto.view_crypto_payment()
                            case 'e':
                                adminFunction()
                            case 'f':
                                domestic_bank=DomesticBankTransfer(domestic_bank)
                                with open(domestic_bank_file,"w") as f:
                                    json.dump(domestic_bank,f,indent=4)
                                print("Successfully Transfer************************")
                                
                            case '0':
                                print("***********************************Thanks for using our payment processing system************************************")
                                break
                            case _:
                                print("Invalid option")
                                break
                    break

        case '2':
            signUp_name=input("Enter Your name: ")
            signUp_email=input("Enter Your Email: ")
            signUp_password=input("Enter Your Password: ")
            signUp_phone=input("Enter Your Phone Number: ")
            singUp_address=input("Enter Your address")
            singup_list.append({
                "name":signUp_name,
                "email":signUp_email,
                "password":signUp_password,
                "phone":signUp_phone,
                "address":singUp_address,
                "datetime":datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            })
            with open(signUp_file,"w") as f:
                json.dump(singup_list,f,indent=4)
            print("Sing Up successfully completed*******************")
