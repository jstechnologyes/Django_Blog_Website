from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
# Create your views here.

def home(request, year, month):
   name="Hadiuzzaman"
   
   month_number= int(month_number)
   cal = HTMLCalendar().formatmonth(year, month_number)
   return render(request,'home.html',{'name':name, 'year':year,'month':month,'month_number':month_number,'cal':cal})