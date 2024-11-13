from django.db import models
from gtts import gTTS


class Word(models.Model):
    word = models.CharField(max_length=100, unique=True)
    meaning = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word

class Pronunciation(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='pronunciations/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.word}"
    
    def save(self, *args, **kwargs):
        tts = gTTS(text=self.word.word, lang='en')
        filename = f"{self.word.word}.mp3"
        tts.save(filename)
        self.audio_file = filename
        super().save(*args, **kwargs)