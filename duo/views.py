from django.shortcuts import render
from django.http import JsonResponse

from .models import Sentence


def index(request):
    return render(request, 'duo/index.html')


def search(request):
    query = request.GET.get('query')
    data = []
    if query:
        sentences = Sentence.objects.raw('''
            select * from duo_sentence
            where english &@ '%s'
            or japanese &@ '%s'
            limit 10
        ''', [query, query])
        data = [
            {
                'japanese': s.japanese,
                'english': s.english
            }
            for s in sentences
        ]

    return JsonResponse({
        'result': data,
    })
