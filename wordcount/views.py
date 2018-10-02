from django.http import HttpResponse
from django.shortcuts import render
import operator


def about(request):
    return render(request, 'about.html')


def home(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']  # This will return whatever the client enters in the textarea tag in home.html

    wordlist = fulltext.split()  # This will make a list with each word in the fulltext variable as separate entries

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            # increase
            worddictionary[word] += 1
        else:
            # add to the dictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'sortedwords': sortedwords})