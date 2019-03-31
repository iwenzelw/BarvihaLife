from django.db import models

class Room(models.Model):
    title = models.CharField(max_length=255, default='', blank=True)
    tittle = models.CharField(max_length=255, default='', blank=True)
    titttle = models.CharField(max_length=255, default='', blank=True)
    description = models.TextField(default='', blank=True)

    def __str__(self):
        return '%s %s %s %s' % (self.title, self.tittle, self.titttle, self.description)
