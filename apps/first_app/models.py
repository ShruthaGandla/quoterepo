from __future__ import unicode_literals
from django.db import models
import re,bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def registration(self,name,alias,email,password,conpassword):
        errormessages =[]
        if not name or len(name)<2 or not name.isalpha():
            errormessages.append("InValid name.Should contain only alphabets atleast 2")
        if not alias or len(alias)<2 or not alias.isalpha():
            errormessages.append("InValid alias.Should contain only alphabets atleast 2")
        if not email or not EMAIL_REGEX.match(email):
            errormessages.append("InValid email")
        if password != conpassword:
            errormessages.append("password mismatch")
        if len(password)<8:
            errormessages.append("password length atleast 8")

        if not errormessages:
            myString =""
            mypassword = password.encode()
            hashed = bcrypt.hashpw(mypassword,bcrypt.gensalt())
            myString =hashed
            return myString
        else:
            return errormessages

    def login(self,userPassword,password):
        dabasePassword = userPassword.encode()
        mypassword = password.encode()
        if(bcrypt.hashpw(mypassword,dabasePassword)==dabasePassword):
            return True
        else:
            return False
    def createQuoteLogic(self,quotedBy,message):
        errormessages =[]
        if not quotedBy or len(quotedBy)<4:
            errormessages.append("quted by field Should contain only alphabets atleast 4")
        if not message or len(message)<11 :
            errormessages.append("Message should contain atleast 10 characters and cannot be empty")
        if not errormessages:
            result ="success"
            return result
        else:
            return errormessages




class User(models.Model):
    name = models.CharField(max_length=45)
    alias = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Quote(models.Model):
    quote_content = models.CharField(max_length=45)
    user = models.ForeignKey(User, related_name="all_quotes")
    favourite=models.ManyToManyField(User,related_name='fav_list')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
