from django.contrib import admin
from django.urls import path
from api.views import WordListCreate, get_pronunciation, get_word_meaning, search_word

urlpatterns = [
    path('words/', WordListCreate.as_view(), name='word-list-create'),
    path('words/<str:word>/', get_word_meaning, name='get_word_meaning'),
    path('pronunciation/<str:word>/', get_pronunciation, name='word-pronunciation'),
    path('related_words/<str:word>/', search_word, name="search")
]