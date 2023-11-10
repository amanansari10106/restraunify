
from django.conf import settings
from django.core.mail import send_mail


def sendmail(email, message, subject="Subject"):
    try:
        # message = f'Hi thank you for registering in PLI. \n click on this link : http://127.0.0.1:8000/user/verify/email/{token}/ to verify your account'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )
    except Exception as e:
        print("error")
        print(e)
        return False
    
    return True

    

