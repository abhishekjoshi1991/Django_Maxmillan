from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
'''
    now here instead of passing hard coded path of url, to make it dynamic we can
    user reverse function, reverse function construct url automatically from url name
    
    name argument that we have passed in urls.py file
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

# getting list of clickable months
def index(request):
    list_items = ''
    months = list(challenge.keys())
    for m in months:
        redirect_path = reverse("monthly-challenge", args=[m])
        list_items += f"<h3><li> <a href='{redirect_path}'> {m.capitalize()} </a></li></h3>"
    return HttpResponse(list_items)

# view to handle url of /mon of type integer
def month_by_number(request, mon):
    months_list = list(challenge.keys())
    try:
        redirect_month = months_list[mon-1]
        # return HttpResponseRedirect('/challenges/' + redirect_month)
        # instead of above, write following
        # syntax: reverse(viewname, args)
        redirect_path = reverse("monthly-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)

    except:
        return HttpResponseNotFound('Month not found!!!')


# view to handle url of /mon of type string
def month(request, mon):
    try:
        challenge_text = challenge.get(mon)
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('Month is not supported!')


