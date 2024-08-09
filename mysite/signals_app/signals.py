from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver

from django.db.models.signals import pre_init

#reciever
# def login_success(sender,request,user,**kwargs):
#     print(" I am user logged in signal")
#     print("sender",sender)
#     print("request",request)
#     print("user",user)
#     print("kwargs",kwargs)
#     # logic to send mail
#     # connect to any s3 bucket and store logs over there
#     #implement any notification

# user_logged_in.connect(login_success, sender=User)

# @receiver(user_logged_out,sender=User)
# def log_out(sender,request,user,**kwargs):
#     print("I am user logged out signal")
#     print("sender",sender)
#     print("request",request)
#     print("user",user)
#     print("kwargs",kwargs)


# @receiver(user_login_failed)
# def login_failed(sender,request,credentials,**kwargs):
#     print("I am user login failed signal")
#     print("sender",sender)
#     print("request",request)
#     print("credentials",credentials)
#     print("kwargs",kwargs)


# @receiver(pre_init, sender=User)
# def before_interaction_with_model(sender,*args,**kwargs):
#     print("I am pre_init signal")
#     print("sender",sender)
#     print("args",args)
#     print("kwargs",kwargs)
