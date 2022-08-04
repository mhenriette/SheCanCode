
from email import message
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
from .forms import FormSignup
from .models import Signup

class HttpResponseError:
    pass


def home(request):  
  return render(request, 'home.html')


def account(request):
  if request.method == 'POST':
    username = request.POST.get('uname')  # takes user input
    userpassword = request.POST.get('password')  #takes user password (input)
  else:
    return redirect('home')
 

    # fname= Signup.objects.filter(fname=username).values('password')
  fname= Signup.objects.filter(fname=username)
  for i in fname:
   upass= i.password
    #  request.session['upass'] = upass
   if (userpassword==upass):
      
    context = {
        'fname': i.fname,
        'balance': i.balance,
      }
     
    return render(request, 'account.html', context)

     
  return render(request, 'account.html', context)


def signup(request):
    form = FormSignup(request.POST or None)
    if request.method =='POST':

      if form.is_valid():
        form.save()
      return render(request, 'registered.html')
    else:
     form = FormSignup()
    context = {
        'form': form
    } 
    return render(request, 'signup.html', context)


def sendmoney():
  username = request.POST.get('uname')  # takes user input
  amount = request.POST.get('password')  #takes user password (input)
  balance = balance - amount 
  message = "Money sent successfuly"
  return message
