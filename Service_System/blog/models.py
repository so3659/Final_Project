from django.conf import settings
from django.db import models
from django.utils import timezone
from gtts import gTTS
import os


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    image = models.ImageField(upload_to='blog_image/%Y/%m/%d/', default='blog_image/default_error.png')
    audio_file = models.FileField(upload_to='blog/audio/', blank=True, null=True)



    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title

    def generate_audio(self):
        if self.text:
            tts = gTTS(text=self.text, lang='ko')
            audio_path = f'media/blog/audio/post_{self.id}.mp3'
            tts.save(audio_path)
            self.audio_file = f'blog/audio/post_{self.id}.mp3'
            self.save()