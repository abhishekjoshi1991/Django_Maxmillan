from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

# URL and Views

'''
URL: Ensures that certain results are achieved when some URL is hit by user
VIEWS: The logic executed for different urls
'''

challenge ={
    'january': 'learn django',
    'february': 'learn python',
    'march': 'learn react',
    'april': 'learn html',
    'may': 'learn css',
    'june': 'learn javascript',
    'july': 'learn git ',
    'august': 'learn flask',
    'september': 'learn aws',
    'october': 'learn server',
    'november': 'learn pandas',
    'december': 'learn numpy'
}

# view to handle url of /month
def index(request, month):
    challenge_text = challenge.get(month)
    if challenge_text:
        return HttpResponse(challenge_text)
    else:
        return HttpResponseNotFound('Month is not supported!')


# view to handle url of /mon of type integer
def month_by_number(request, mon):
    return HttpResponse(mon)

'''
instead of returning month number, will redirect to respective month
e.g. new/1 will redirect to january
that we will cover in next project'''


# view to handle url of /mon of type string
def month(request, mon):
    try:
        challenge_text = challenge.get(mon)
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('Month is not supported!')