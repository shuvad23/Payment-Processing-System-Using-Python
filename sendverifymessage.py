import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()
paymentmethod_list=["Credit Card Payment","Paypaly Payment","Cash Payment","Crypto Payment"]

#sending message via whatsapp------------------------------------------------------------
def client_notification_message(index_number,transcation_id,amount,phone):
    account_sid=os.getenv("ACCOUNT_SID")  # Get the account SID from environment variable
    if not account_sid:
        print("Account SID is not set. Please set the ACCOUNT_SID environment variable.")
        return
    auth_token=os.getenv("AUTH_TOKEN")  # Get the auth token from environment variable
    if not auth_token:
        print("Auth token is not set. Please set the AUTH_TOKEN environment variable.")
        return
    admin_number= os.getenv("TWILIO_NUMBER")  # Get the Twilio number from environment variablei
    if not admin_number:
        print("Twilio number is not set. Please set the TWILIO_NUMBER environment variable.")
        return
    recipient_number="whatsapp:"+phone
    client=Client(account_sid,auth_token)
    try:
        message=client.messages.create(
            body=("Payment Confirmation Message:"
                "\nDear [xxxxx],"
                f"\nYour payment of [{amount}] has been successfully received."
                f"\nTransaction ID: [{transcation_id}]."
                f"\nPayment was made using [{paymentmethod_list[index_number]}] linked to Phone: [{phone}]."
                "\nIf you have any questions, please contact us."
                "\nThank you for your trust!"),
            from_=admin_number,
            to=recipient_number
        )
        print("Payment notificaton has been successfully sended to Client")
    except Exception as e:
        print("An error Occurred")

#sending messages via telegram -----------------------------------------------------------------

def admin_verificaton_message(index_number,transcation_id,amount,phone):
    bot_token=os.getenv("ACCOUNT_TOKEN")  # Get the bot token from environment variable
    if not bot_token:
        print("Bot token is not set. Please set the ACCOUNT_TOKEN environment variable.")
        return
    chat_id = os.getenv("CHAT_ID")  # Get the chat ID from environment variable
    if not chat_id:
        print("Chat ID is not set. Please set the CHAT_ID environment variable.")
        return
    message_body=(f"Dear Admin, a payment has been made successfully."
                  f"\nTransaction ID: {transcation_id}"
                  f"\nName: XXXXX | Payment Method: {paymentmethod_list[index_number]} | Phone: {phone}"
                  f"\nAmount: TK.{amount}"
                  "\nPlease verify and confirm the transaction. Thank you!")
    telegram_url_link=f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload={"chat_id":chat_id,"text":message_body}
    try:
        response=requests.post(url=telegram_url_link,json=payload)
        print("Payment notificaton has been successfully sended to Admin")
    except Exception as e:
        print("An error Occurred")