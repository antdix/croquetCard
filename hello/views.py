from django.shortcuts import render
from django.http import HttpResponse
import requests

# Import modules for CGI handling 
import cgi, cgitb

import subprocess
from subprocess import Popen, PIPE

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def cash(request):
    # Returns a dictionary in which the values are lists

    params = request.GET
    MyHandicap = params['MyHandicap']
    MyIndex = params['MyIndex']
    oppoHandicap1 = params['OppoHandicap1']
    gameType1 = params['GameType1']
    result1 = params['Result1']
    indexChange1 = '+6'
    newIndex1 = '2345'
    outStr = '<body>' \
              '<center><TABLE COLS=4\n border=3>'  \
              '<TR>' \
              '<TD><center> Game <center>' \
              '<TD><center> Oppo Handicap <center>' \
              '<TD><center> Handicap/Level <center>' \
              '<TD><center> Result <center>' \
              '<TD><center> IndexChange <center>' \
              '<TD><center> NewIndex <center>' \
              '<TR>' \
              '<TD><center> 1 <center>' \
              '<TD><center>' + oppoHandicap1 + '<center>' \
              '<TD><center>' + gameType1 + '<center>' \
              '<TD><center>' + result1 + '<center>' \
              '<TD><center>' + indexChange1 + '<center>' \
              '<TD><center>' + newIndex1 + '<center>' \
              '</body>' 

    return HttpResponse(outStr)


#def index(request):
#    r = requests.get('http://httpbin.org/status/418')
#    print(r.text)
#    return HttpResponse('<pre>' + r.text + '</pre>')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
