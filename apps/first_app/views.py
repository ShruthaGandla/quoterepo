from django.shortcuts import render,redirect
from .models import User,Quote
from django.contrib import messages
from django.db.models import Count

def index(request):
    return render(request,"first_app/index.html")
def registrationLogic(request):
    if request.method == 'POST':
        result = User.objects.registration(request.POST['name'],request.POST['alias'],request.POST['email'],request.POST['password'],request.POST['confirm_password'])
        if isinstance(result,str):
            print result
            userInstance=User.objects.create(name = request.POST['name'],alias = request.POST['alias'],email=request.POST['email'],password=result,birthday=request.POST['birthday'])
            request.session['id'] = userInstance.id
            # messages.success(request, 'Succesfully registered or(logged in)')
            return redirect('/quotes')
        elif isinstance(result,list):
            for message in result:
                messages.error(request, message)
            return redirect('/')
def loginLogic(request):
    if request.method == 'POST':
        try:
            userList = User.objects.filter(email=request.POST['email'])
            if(User.objects.login(userList[0].password,request.POST['password'])):
                # messages.success(request, 'Succesfully registered or(logged in)')
                request.session['id'] = userList[0].id
                return redirect('/quotes')
            else:
                messages.error(request, 'Incorrect Password')
                return redirect('/')
        except:
            messages.error(request, 'Incorrect Email ID')
            return redirect('/')
def quotesLogic(request):
    userInstance = User.objects.get(id=request.session['id'])
    quotesList = Quote.objects.all()
    context = {'userInstance':userInstance,
                'quotesList':quotesList}
    return render(request,"first_app/quotes.html",context)

def createQuoteLogic(request):
    if request.method == 'POST':
        result= User.objects.createQuoteLogic(request.POST['quotedby'],request.POST['message'])
        if isinstance(result,list):
            for message in result:
                messages.error(request, message)
            return redirect('/quotes')
        else:
            userInstance = User.objects.get(id=request.session['id'])
            message = request.POST['quotedby']+":"+request.POST['message']
            Quote.objects.create(quote_content=message,user=userInstance)

    return redirect('/quotes')

def userDataLogic(request,id):
    userInstance = User.objects.get(id=id)
    context = {'userInstance':userInstance}


    return render(request,"first_app/userData.html",context)


def addLogic(request,id):
    userInstance = User.objects.get(id=request.session['id'])
    quoteInstance = Quote.objects.get(id = id)
    quoteInstance.favourite.add(userInstance)
    return redirect('/quotes')


def deleteLogic(request,id):
    userInstance = User.objects.get(id=request.session['id'])
    quoteInstance = Quote.objects.get(id = id)
    quoteInstance.favourite.remove(userInstance)
    return redirect('/quotes')
