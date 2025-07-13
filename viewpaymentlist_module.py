import json
def viewAllpaymentList(serial,adminFile):
    from PaymentProcessingSystem import CreditCardPayment,PayPalPayment,CashPayment,CryptoPayment
    email=input('Enter Admin Email: ')
    phone=input("Enter Admin Phone: ")
    count=0
    with open(adminFile,'r') as f:
        data=json.load(f)
        for admin in data:
            if (email in admin['email']) and (phone in admin['phone']):
                if(serial=='a'):
                    cc_payment=CreditCardPayment("","","","","","")
                    cc_payment.view_creditcard_payment()
                    count=0
                    break
                elif(serial=='b'):
                    pp_payment=PayPalPayment("","","","","")
                    pp_payment.view_paypal_payment()
                    count=0
                    break
                elif(serial=='c'):
                    cash_payment=CashPayment("","","")
                    cash_payment.view_cash_payment()
                    count=0
                    break
                elif(serial=='d'):
                    crypto_payment=CryptoPayment("","","","")
                    crypto_payment.view_crypto_payment()
                    count=0
                    break
            else:
                count+=1
        if(count>=1):
            print("Your Email and Phone Number not match")               
    
def viewSinglePayment():
    pass