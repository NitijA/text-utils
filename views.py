# I have created this file - Nitij
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'homepage.html')

def analyze(request):
    #Get text
    dj_text = request.POST.get('text', 'default')
    #Check Checkbox Values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    #Check which checkbox is ON
    if removepunc == 'on':
        analyzed = ""
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in dj_text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'analysed_text' : analyzed}
        dj_text = analyzed


    if fullcaps =='on':
        analyzed = ''
        for char in dj_text:
            analyzed = analyzed + char.upper()
        params = {'analysed_text': analyzed}
        dj_text = analyzed


    if newlineremover == 'on':
        analyzed = ''
        for char in dj_text:
            if char != '\n' and char != '\r':
                analyzed = analyzed +char
        params = {'analysed_text': analyzed}
        dj_text = analyzed


    if spaceremover == 'on':
        analyzed = ''
        for char in dj_text:
            if char != ' ':
                analyzed = analyzed + char
        params = {'analysed_text': analyzed}
        dj_text = analyzed


    if extraspaceremover == 'on':
        analyzed = ''
        for i, char in enumerate(dj_text):
            if not(dj_text[i] == ' ' and dj_text[i+1] == ' '):
                if dj_text == '':
                    break
                analyzed = analyzed + char
        params = {'analysed_text': analyzed}
        dj_text = analyzed


    if charcount == 'on':
        analyzed = ''
        for char in dj_text:
            analyzed = analyzed + char
        count = len(analyzed)
        params = {'purpose': 'No. Of Characters In Your String', 'analysed_text': analyzed, 'count' : count}
        return render(request, 'analyze2.html', params)

    if (removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and spaceremover != 'on' and extraspaceremover != 'on' and charcount != 'on'):
        return HttpResponse('To Analyze Text, Please Toggle the Relevent Switch.   <a href = "http://127.0.0.1:8000/"> Go Back </a>')

    return render(request, 'analyse.html', params)