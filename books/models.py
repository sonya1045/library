from django.db import models

class LibraryBook(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    isbn = models.CharField(max_length=30)
    available = models.BooleanField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['author']
        unique_together = [['isbn']]