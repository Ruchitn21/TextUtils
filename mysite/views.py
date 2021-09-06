
from django.http import HttpResponse
from django.shortcuts import render
import requests

def index(request):

    return render(request,"index.html")


def analyze(request):

    djtext= request.POST.get("text","default")

    removepunc= request.POST.get("removepunc","off")
    fullcaps= request.POST.get("fullcaps","off")
    newlineremover= request.POST.get("newlineremover","off")
    extraspaceremover= request.POST.get("extraspaceremover","off")

    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        text= ""
        for i in djtext:
            if i not in punctuations:
                text+=i
        
        params= {"purpose":"Removing Punctuations", "analyzed_text":text}

        djtext= text

        # return render(request,"analyze.html",params)
    
    if fullcaps=="on":

        text= djtext.upper()

        params= {"purpose":"Capitalizing Text", "analyzed_text":text}

        djtext= text
        # return render(request,"analyze.html",params)
    
    if extraspaceremover=="on":

        text= ""

        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                text+=char
        
        params= {"purpose":"Removing Extra Spaces", "analyzed_text":text}

        djtext= text

        # return render(request,"analyze.html",params)
    
    if newlineremover == "on":
        
        analyzed = ""

        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

        djtext= analyzed
    
    if removepunc!="on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on":
        return HttpResponse("Error...Please choose any operation")
    
    return render(request, 'analyze.html', params)

    
    
