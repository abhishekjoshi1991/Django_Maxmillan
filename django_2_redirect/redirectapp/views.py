from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.
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


# view to handle url of /mon of type integer
def month_by_number(request, mon):
    months_list = list(challenge.keys())
    try:
        redirect_month = months_list[mon-1]
        return HttpResponseRedirect('/challenges/' + redirect_month)

        '''
        now here we have passed hard coded path of url /challenges/, to make it dynamic we can
        user reverse function, reverse function construct url automatically from url name
        '''
    except:
        return HttpResponseNotFound('Month not found!')


# view to handle url of /mon of type string
def month(request, mon):
    try:
        challenge_text = challenge.get(mon)
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('Month is not supported!')