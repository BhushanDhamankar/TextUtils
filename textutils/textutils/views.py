from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    analyzed=""
    djtext=request.GET.get('text', 'default')
    up=request.GET.get('uppercase', 'off')
    low=request.GET.get('lowercase', 'off')
    punc=request.GET.get('removepunc', 'off')
    space=request.GET.get('spaceremover', 'off')
    flag = 0
    if(up == 'on'):
        flag = 1
        for char in djtext:
            analyzed = analyzed + char.upper()
        djtext = analyzed
        analyzed = ""
    if(low == 'on'):
        flag = 1
        for char in djtext:
            analyzed = analyzed + char.lower()
        djtext = analyzed
        analyzed = ""
    if(punc == 'on'):
        flag = 1
        punc=['-', '|', ',', ':', ';', '?', '/', '_']
        for char in djtext:
            if char in punc:
                continue
            else:
                analyzed = analyzed + char
        djtext = analyzed
        analyzed = ""
    if(space == 'on'):
        flag = 1
        for char in djtext:
            if(char == ' '):
                continue
            else:
                analyzed = analyzed +char
        djtext=analyzed
    result={'analyzed' : djtext }
    return render(request,'analyze.html',result)


