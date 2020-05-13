from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')
def name(request):
    return HttpResponse('<h1> Harshal</h1>')
def about(request):
    return render(request,'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word]+=1
        else:
            worddictionary[word]=1
    sortednumbers = sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=False)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortednumbers':sortednumbers})
