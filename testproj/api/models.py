from django.db import models

class Message(models.Model):
    author=models.EmailField(max_length=50)
    text=models.TextField(max_length=100)
    publicatedate=models.DateTimeField(auto_now_add=True)
    updatedate=models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return self.author
