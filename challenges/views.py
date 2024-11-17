from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
#from django.template.loader import render_to_string

monthly_challenges = {
    'january' : 'Eat no meat for a month',
    'febraury' : 'Walk for atleast 20 minutes everyday',
    'march' : 'Learn Django for atleast 20 minuts every day!',
    'april' : 'Eat no meat for a month',
    'may' : 'Walk for atleast 20 minutes everyday',
    'june' : 'Learn Django for atleast 20 minuts every day!',   
    'july' : 'Eat no meat for a month',
    'august' : 'Walk for atleast 20 minutes everyday',
    'september' : 'Learn Django for atleast 20 minuts every day!',
    'october' : 'Eat no meat for a month',
    'november' : 'Walk for atleast 20 minutes everyday',
    'december' : None,
}
# Create your views here

def index(request):
    months = list(monthly_challenges.keys())
    return render(request, 'challenges/index.html', {'months' : months})

def index_monthly_challenge_by_number(request, month):
   months = list(monthly_challenges.keys())

   if month > len(months):
      return HttpResponseNotFound('Invalid month')

   redirect_month = months[month-1]
   redirect_path = reverse('monthly-challenge', args = [redirect_month]) 

   return HttpResponseRedirect(redirect_path)

def index_monthly_challenge(request, month):
    try:    
      challenge_text = monthly_challenges[month]
      # response_data = render_to_string('challenges/challenge.html')
      # return HttpResponse(response_data)
      return render(request, 'challenges/challenge.html', { 'text' : challenge_text, 'month_name' : month })
    except:
       return render(request, '404.html')
       #return HttpResponseNotFound('<h1> This month {0} is not supported </h1>'.format(month))