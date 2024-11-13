from django.contrib import admin
from .models import Word, Pronunciation

class WordAdmin(admin.ModelAdmin):
    list_display = ('word', 'meaning')
    search_fields = ('word',)
    list_filter = ('word',)

class PronunciationAdmin(admin.ModelAdmin):
    list_display = ('word', 'audio_file')
    search_fields = ('word',)
    list_filter = ('word',)

admin.site.register(Word, WordAdmin)

admin.site.register(Pronunciation, PronunciationAdmin)