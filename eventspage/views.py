from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from django.template import loader
from eventspage.models import Member
from sanmail import sendmail
import time

def members(request):
  template = loader.get_template('h1.html')
  return HttpResponse(template.render())
# Create your views here.

def reg(request):
  form = RegistrationForm(request.GET)
  if form.is_valid():
    # Process the form data and save it if needed
    name = form.cleaned_data['name']
    email = form.cleaned_data['email']
    session = "Sangeeth Session 7" #Change This Field
    members = Member(firstname=name,email=email,session=session)
    members.save()
    print(name)
    print(email)
    '''
    Sample Method to Send Mail:
    Date = September 21
    Date1 = September 21st
    Day = Thursday
    Year = 2023
    Send in String Format

    '''
    date = 'November 22'
    date1 = 'November 22nd'
    Day = 'Wednesday'
    year = '2023'
    sendmail(name,email,date,date1,Day,year)
    time.sleep(300)
    # Redirect to the homepage after processing the form
    return redirect('home')  # 'home' is the name of the URL pattern for the homepage
  else:
    form = RegistrationForm()
    name =''
    email = ''
 
  return render(request, 'registration.html', {'form': form})
  
  
