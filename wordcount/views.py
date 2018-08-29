from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def count(request):
    textvalue = request.GET['fulltext']
    wordlist = textvalue.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    return render(request, 'count.html', {'fulltext': textvalue, 'count': len(wordlist),
                                          'word_dictionary': sorted(worddictionary.iteritems(), key=lambda(k, v): (v, k)})
