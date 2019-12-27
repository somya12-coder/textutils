#i hv created this file first of all file is to be created
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def analyze(request):
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')
    print(removepunc)
    print(djtext)

    if(removepunc=='on'):
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
              analyzed = analyzed + char
        djtext=analyzed
        params = { 'analyzed_text': analyzed}


    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        djtext=analyzed
        params = { 'analyzed_text': analyzed}

    if (extraspaceremover == 'on'):

        analyzed = ""
        for index,char in enumerate (djtext):
            if not( djtext[index]==" "and djtext[index+1]==" "):
                analyzed = analyzed + char
        djtext = analyzed
        params = {'analyzed_text': analyzed}

    else:
         return HttpResponse("Error")

    return render(request,"analyze.html",params)
 #   return  HttpResponse('<h2> lets explore more grow more</h2><a href=" http://127.0.0.1:8000/">BACK</a>')