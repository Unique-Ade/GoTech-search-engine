from rest_framework import generics
from .models import Word, Pronunciation
from .serializers import WordSerializer
from gtts import gTTS
import os
from django.http import JsonResponse
from rest_framework import status


class WordListCreate(generics.ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    


def get_word_meaning(request, word):
    try:
        word_obj = Word.objects.get(word=word)
        return JsonResponse({'meaning': word_obj.meaning},status = status.HTTP_200_OK)  
    except Word.DoesNotExist:
        return JsonResponse({'error': 'Word not found'}, status=status.HTTP_404_NOT_FOUND)

def search_word(request, word):
    try:
        related_words = Word.objects.filter(word__icontains=word)[:3]
        return JsonResponse({'related_words': [word.word for word in related_words]}, status=status.HTTP_200_OK)
    except Word.DoesNotExist:
        return JsonResponse({'error': 'Word not found'}, status=status.HTTP_404_NOT_FOUND)

