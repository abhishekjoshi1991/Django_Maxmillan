from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

challenge = {
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


# getting list of clickable months
# for loop in DTL is used in below view and dynamic url in .html
def index(request):
    list_items = ''
    months = list(challenge.keys())
    return render(request, 'demo/index.html', {'months': months})


# view to handle url of /mon of type integer
def month_by_number(request, mon):
    months_list = list(challenge.keys())
    try:
        redirect_month = months_list[mon - 1]
        redirect_path = reverse("monthly-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound('Month not found!!!')


# view to handle url of /mon of type string
# DTL used in below view, filter used in challenge.html

def month(request, mon):
    try:
        challenge_text = challenge.get(mon)
        return render(request, 'demo/challenge.html', {'challenge_text': challenge_text, 'month': mon})
    except:
        return HttpResponseNotFound('Month is not supported!')


