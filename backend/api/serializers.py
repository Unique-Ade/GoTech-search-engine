from rest_framework import serializers
from .models import Word, Pronunciation

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'word', 'meaning']

class PronunciationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pronunciation
        fields = ['id', 'word', 'audio_file']