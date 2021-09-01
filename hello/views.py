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

def pointsWin(oppoHandicap, MyHandicap, stepDiff, gameType):
    if gameType == "Handicap":
        return (10)
    elif oppoHandicap > MyHandicap:
        if stepDiff <= 6:
            return (20 - (10 + stepDiff))
        elif stepDiff == 7 or stepDiff == 8:
            return (3)
        elif stepDiff == 9 or stepDiff == 10:
            return (2)
        else:
            return (1)
    else:
        if stepDiff <= 6:
            return (10 + stepDiff)
        elif stepDiff == 7 or stepDiff == 8:
            return (17)
        elif stepDiff == 9 or stepDiff == 10:
            return (18)
        else:
            return (19)

def pointsLose(oppoHandicap, MyHandicap, stepDiff, gameType):
    if gameType == "Handicap":
        return (-10)
    elif oppoHandicap < MyHandicap:
        if stepDiff <= 6:
            return ((20 - (10 + stepDiff)) * -1)
        elif stepDiff == 7 or stepDiff == 8:
            return (-3)
        elif stepDiff == 9 or stepDiff == 10:
            return (-2)
        else:
            return (-1)
    else:
        if stepDiff <= 6:
            return ((10 + stepDiff) * -1)
        elif stepDiff == 7 or stepDiff == 8:
            return (-17)
        elif stepDiff == 9 or stepDiff == 10:
            return (-18)
        else:
            return (-19)

def stepsfromZero(handicap):
    if handicap == -3.0:
        return (-21)
    elif handicap == -2.5:
        return (-16)
    elif handicap == -2.0:
        return (-12)
    elif handicap == -1.5:
        return (-8)
    elif handicap == -1.0:
        return (-5)
    elif handicap == -0.5:
        return (-2)
    elif handicap <= 5:
        return (int(handicap * 2))
    elif handicap <= 12:
        return (int(handicap + 5))
    else:
        return (int(((handicap - 12) * 0.5) + 17))

def calculateNewIndex (oppoHandicap, gameType, result, MyHandicap, newIndex):
    oppoSteps = stepsfromZero(oppoHandicap)
    mySteps = stepsfromZero(MyHandicap)
    stepDiff = abs(oppoSteps - mySteps)
    #print ("My Steps {} oppo  Steps {} stepDiff {} result {} OH {} MH {}".format(mySteps, oppoSteps, stepDiff, result, oppoHandicap, MyHandicap))
    if result == "Win":
        indexChange = pointsWin(oppoHandicap, MyHandicap, stepDiff, gameType)
    else:
        indexChange = pointsLose(oppoHandicap, MyHandicap, stepDiff, gameType)
    #print ("indexChange {}".format(indexChange))

    newIndex += indexChange
    NI = int (newIndex)
    
    return (str(indexChange), str(NI))

def calculate(request):
    # Returns a dictionary in which the values are lists

    params = request.POST
    MyHandicap = params['MyHandicap']
    MyIndex = params['MyIndex']

    try:
        newIndex = float(MyIndex)
    except:
        outStr = '<body> <center> <h1> Please enter a valid Index </h1> '  
        outStr = outStr + '</table><button onclick="goBack()">Go Back</button>' \
                               ' <script>' \
                               '     function goBack() {' \
                               '         window.history.back(); ' \
                               '     } '\
                               ' </script> '
        outStr = outStr + '</body>' 
        return HttpResponse(outStr)

    if newIndex > 3500:
        outStr = '<body> <center> <h1> Please enter a valid Index </h1> '  
        outStr = outStr + '</table><button onclick="goBack()">Go Back</button>' \
                               ' <script>' \
                               '     function goBack() {' \
                               '         window.history.back(); ' \
                               '     } '\
                               ' </script> '
        outStr = outStr + '</body>' 
        return HttpResponse(outStr)

    oppoHandicaps = []
    gameTypes = []
    results = []

    oppoHandicaps.append(params['OppoHandicap1'])
    oppoHandicaps.append(params['OppoHandicap2'])
    oppoHandicaps.append(params['OppoHandicap3'])
    oppoHandicaps.append(params['OppoHandicap4'])
    oppoHandicaps.append(params['OppoHandicap5'])
    oppoHandicaps.append(params['OppoHandicap6'])
    oppoHandicaps.append(params['OppoHandicap7'])
    oppoHandicaps.append(params['OppoHandicap8'])
    oppoHandicaps.append(params['OppoHandicap9'])
    oppoHandicaps.append(params['OppoHandicap10'])

    gt = "Level"
    try:
        gt = params['GameType1']
    except:
        pass
    gameTypes.append(gt)

    res = "Lose"
    try:
        res = params['Result1']
    except:
        pass
    results.append(res)


    gt = "Level"
    try:
        gt = params['GameType2']
    except:
        pass
    gameTypes.append(gt)

    res = "Lose"
    try:
        res = params['Result2']
    except:
        pass
    results.append(res)

    gt = "Level"
    try:
        gt = params['GameType3']
    except:
        pass
    gameTypes.append(gt)

    res = "Lose"
    try:
        res = params['Result3']
    except:
        pass
    results.append(res)

    gt = "Level"
    try:
        gt = params['GameType4']
    except:
        pass
    gameTypes.append(gt)

    res = "Lose"
    try:
        res = params['Result4']
    except:
        pass
    results.append(res)

    gt = "Level"
    try:
        gt = params['GameType5']
    except:
        pass
    gameTypes.append(gt)

    res = "Lose"
    try:
        res = params['Result5']
    except:
        pass
    results.append(res)

    gt = "Level"
    try:
        gt = params['GameType6']
    except:
        pass
    gameTypes.append(gt)

    res = "Lose"
    try:
        res = params['Result6']
    except:
        pass
    results.append(res)

    gt = "Level"
    try:
        gt = params['GameType7']
    except:
        pass
    gameTypes.append(gt)

    res = "Lose"
    try:
        res = params['Result7']
    except:
        pass
    results.append(res)

    gt = "Level"
    try:
        gt = params['GameType8']
    except:
        pass
    gameTypes.append(gt)

    res = "Lose"
    try:
        res = params['Result8']
    except:
        pass
    results.append(res)

    gt = "Level"
    try:
        gt = params['GameType9']
    except:
        pass
    gameTypes.append(gt)

    res = "Lose"
    try:
        res = params['Result9']
    except:
        pass
    results.append(res)

    gt = "Level"
    try:
        gt = params['GameType10']
    except:
        pass
    gameTypes.append(gt)

    res = "Lose"
    try:
        res = params['Result10']
    except:
        pass
    results.append(res)

    indexChange1 = '+6'
    newIndex1 = '2345'
    outStr = '<body>' \
              '<center><TABLE border=3>'  \
              '<TR>' \
              '<TD><center> Game' \
              '<TD><center> Oppo Handicap' \
              '<TD><center> Handicap/Level <center>' \
              '<TD><center> Result <center>' \
              '<TD><center> IndexChange <center>' \
              '<TD><center> NewIndex <center>' \

    for i in range(0,10):
        if oppoHandicaps[i] != "":
            indexChange,newIndex = calculateNewIndex (float(oppoHandicaps[i]), gameTypes[i], results[i], float(MyHandicap), float(newIndex))
            outStr = outStr + '<TR><TD><center>' + str(i+1) + ''\
              '<TD><center>' + oppoHandicaps[i] + '' \
              '<TD><center>' + gameTypes[i] + '' \
              '<TD><center>' + results[i] + '' \
              '<TD><center>' + indexChange + '' \
              '<TD><center>' + newIndex + '' 

    outStr = outStr + '</table><br><button onclick="goBack()">Go Back</button>' \
                               ' <script>' \
                               '     function goBack() {' \
                               '         window.history.back(); ' \
                               '     } '\
                               ' </script> '
    outStr = outStr + '</body>' 

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
