import json
import uuid
from datetime import datetime

indian_banks_branches=[]
bangladesh_banks_branches=[]
uk_banks_branches=[]
usa_banks_branches=[]
german_banks_branches=[]

with open("data/indian_banks_branches.json","r") as f1:
    indian_banks_branches=json.load(f1)
with open("data/bangladesh_banks_branches.json","r") as f:
    bangladesh_banks_branches=json.load(f)
with open("data/uk_banks_branches.json","r") as f:
    uk_banks_branches=json.load(f)
with open("data/usa_banks_branches.json","r") as f:
    usa_banks_branches=json.load(f)
with open("data/german_banks_branches.json","r") as f:
    german_banks_branches=json.load(f)


indian_top_banks = [
    "State Bank of India",
    "HDFC Bank",
    "ICICI Bank",
    "Punjab National Bank",
    "Axis Bank",
    "Kotak Mahindra Bank",
    "Bank of Baroda",
    "Canara Bank",
    "Union Bank of India",
    "IndusInd Bank"
]

#bangladesh**********************************************
top_banks_bangladesh = [
    "Islami Bank Bangladesh PLC",
    "Dutch-Bangla Bank Limited",
    "Sonali Bank PLC",
    "BRAC Bank Limited",
    "Eastern Bank Limited",
    "Standard Chartered Bank",
    "HSBC Bank Bangladesh",
    "City Bank Limited",
    "Pubali Bank Limited",
    "Janata Bank Limited"
]

#UK********************************************
top_banks_uk = [
    "HSBC Holdings",
    "Barclays",
    "Lloyds Bank",
    "NatWest",
    "Standard Chartered",
    "Santander UK",
    "Nationwide Building Society",
    "Royal Bank of Scotland",
    "Halifax",
    "TSB Bank"
]


#usa********************************************
top_us_banks = [
    "JPMorgan Chase & Co.",
    "Bank of America",
    "Citigroup",
    "Wells Fargo",
    "Goldman Sachs",
    "Morgan Stanley",
    "U.S. Bancorp",
    "PNC Financial Services",
    "Truist Financial",
    "Capital One"
]

#germany********************************************
german_banks = [
    "Deutsche Bank",
    "Commerzbank",
    "KfW Bank",
    "DZ Bank",
    "HypoVereinsbank (UniCredit Bank AG)",
    "Landesbank Baden-Württemberg (LBBW)",
    "Norddeutsche Landesbank (Nord/LB)",
    "Bayerische Landesbank (BayernLB)",
    "ING-DiBa",
    "Santander Bank Deutschland"
]



#******************Domestic Bank Transfer***************************

def DomesticBankTransfer(dbank_list):
    """For transferring money within the same country ,you usually need: 
            1.Beneficiary Name(Account holder's full name 
            2.Bank Name (e.g ,XYZ Bank)
            3.Account Number
            4.IFSC CODE (for india) / Sort code(for uk)/ Bank routing number(for bd)/ ACH Routing number(usa)/  IBAN (International Bank Account Number) and BIC (Bank Identifier Code / SWIFT code)(Germany)
            5.Branch Name and Address
            6.Purpose of Payment(optional but recommended)"""
    print(f"{'*'*60} DomesticBank Transfer System {'*'*60}")
    try:
        name=input("Enter the Beneficiary Name(Account holder's full name): ")
        country_name=input("Enter the country name(India/Bangladesh/UK/USA/Germany): ").lower()
        if(country_name=='india'):
            print("Bank Of INDIA: ",indian_top_banks)
            bank_serial_number=int(input("Bank Name (e.g ,XYZ Bank):Select From The List (serial: 1,10): "))
            bank_name=indian_top_banks[bank_serial_number-1]
            account_number=input("Account Number: ")
            IFSC_code=input("Enter IFSC Code (For India): ")
            amount=int(input("Enter the Transfer Amount: "))

            for branch in indian_banks_branches:
                if(branch==bank_name):
                    branch_list=[branchList["branch_name"] for branchList in indian_banks_branches[branch]]
                    print(branch_list)
                    branch_serial_number=int(input("Enter the Branch Name(For India):select from the list:serial: (1,10): "))
                    branch_name=indian_banks_branches[branch][branch_serial_number-1]["branch_name"]
                    branch_address=indian_banks_branches[branch][branch_serial_number-1]["address"]
                    payment_purpose=input("Enter the Purpose of Payment: ")
                    break
        elif(country_name=='bangladesh'):
            print("Bank Of BANGLADESH: ",top_banks_bangladesh)
            bank_serial_number=int(input("Bank Name (e.g ,XYZ Bank):Select From The List (serial: 1,10): "))
            bank_name=top_banks_bangladesh[bank_serial_number-1]
            account_number=input("Account Number: ")
            routing_number=input("Enter Bank Routing Number(For Bangladesh): ")
            amount=int(input("Enter the Transfer Amount: "))

            for branch in bangladesh_banks_branches:
                if(branch==bank_name):
                    branch_list=[branchList["branch_name"] for branchList in bangladesh_banks_branches[branch]]
                    print(branch_list)
                    branch_serial_number=int(input("Enter the Branch Name(For Bangladesh):select from the list:serial: (1,10): "))
                    branch_name=bangladesh_banks_branches[branch][branch_serial_number-1]["branch_name"]
                    branch_address=bangladesh_banks_branches[branch][branch_serial_number-1]["address"]
                    payment_purpose=input("Enter the Purpose of Payment: ")
                    break
            
        elif(country_name=='uk'):
            print("Bank Of UK: ",top_banks_uk)
            bank_serial_number=int(input("Bank Name (e.g ,XYZ Bank):Select From The List (serial: 1,10): "))
            bank_name=top_banks_uk[bank_serial_number-1]
            account_number=input("Account Number: ")
            sort_code=input("Enter the Sort Code(For UK): ")
            amount=int(input("Enter the Transfer Amount: "))

            for branch in uk_banks_branches:
                if(branch==bank_name):
                    branch_list=[branchList["branch_name"] for branchList in uk_banks_branches[branch]]
                    print(branch_list)
                    branch_serial_number=int(input("Enter the Branch Name(For United Kingdom):select from the list:serial: (1,10): "))
                    branch_name=uk_banks_branches[branch][branch_serial_number-1]["branch_name"]
                    branch_address=uk_banks_branches[branch][branch_serial_number-1]["address"]
                    payment_purpose=input("Enter the Purpose of Payment: ")
                    break

        elif(country_name=='usa'):
            print("Bank Of USA: ",top_us_banks)
            bank_serial_number=int(input("Bank Name (e.g ,XYZ Bank):Select From The List (serial: 1,10): "))
            bank_name=top_us_banks[bank_serial_number-1]
            account_number=input("Account Number: ")
            aba_number=input("Enter the ABA Number(Routing Number)(For USA): ")
            amount=int(input("Enter the Transfer Amount: "))
            for branch in usa_banks_branches:
                if(branch in bank_name):
                    branch_list=[branchList["branch_name"] for branchList in usa_banks_branches[branch]]
                    print(branch_list)
                    branch_serial_number=int(input("Enter the Branch Name(For USA):select from the list:serial: (1,10): "))
                    branch_name=usa_banks_branches[branch][branch_serial_number-1]["branch_name"]
                    branch_address=usa_banks_branches[branch][branch_serial_number-1]["address"]
                    payment_purpose=input("Enter the Purpose of Payment: ")
                    break

        elif(country_name=='germany'):
            print("Bank Of Germany: ",german_banks)
            bank_serial_number=int(input("Bank Name (e.g ,XYZ Bank):Select From The List (serial: 1,10): "))
            bank_name=german_banks[bank_serial_number-1]
            account_number=input("Account Number: ")
            IBAN_number=input("Enter the  IBAN (International Bank Account Number)/BIC (Bank Identifier Code / SWIFT code) Number(For Germany): ")
            amount=int(input("Enter the Transfer Amount: "))

            for branch in german_banks_branches:
                if(branch==bank_name):
                    branch_list=[branchList["branch_name"] for branchList in german_banks_branches[branch]]
                    print(branch_list)
                    branch_serial_number=int(input("Enter the Branch Name(For Germany):select from the list:serial: (1,10): "))
                    branch_name=german_banks_branches[branch][branch_serial_number-1]["branch_name"]
                    branch_address=german_banks_branches[branch][branch_serial_number-1]["address"]
                    payment_purpose=input("Enter the Purpose of Payment: ")
                    break
        

    except ValueError as e:
        print("You enter wrong data type | Plz enter the String type data in all the field********")
    
    def add_value(code,code_status,carence):
        dbank_list.append({
            "beneficiary_name": name,
            "bank_name": bank_name,
            "country_name": country_name,
            "account_number":account_number,
            "bank_routing_number":{
                "code":code,
                "code_status":code_status
            },
            "branch_name":branch_name,
            "branch_address":branch_address,
            "transfer_amount":amount,
            "carence":carence,
            "payment_purpose":payment_purpose,
            "transcation_id": str(uuid.uuid4()),
            "datetime":datetime.now().strftime("%B %d %Y, %H:%M:%S")
        })
    if(country_name=='india'):
        add_value(IFSC_code,"IFSC Code(For India)","Rupe")
    elif(country_name=='bangladesh'):
        add_value(routing_number,"Bank Routing Number(For Bangladesh)","TAKA")
    elif(country_name=='uk'):
        add_value(sort_code,"Sort Code(For United Kingdom)","Pound")
    elif(country_name=='usa'):
        add_value(aba_number,"ABA Number(For USA)","Doller")
    elif(country_name=='germany'):
        add_value(IBAN_number,"SEPA((Single Euro Payments Area)) Number (For Europing bank)","Euro")
        
            
    return dbank_list
#******************International Bank Transfer***************************

def InternationalBankTransfer():
    pass