from django.db import models

# Create your models here.
class Side(models.Model):
    text = models.CharField(max_length=10)
    def __str__(self):
        return self.text

class State(models.Model):
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    by = models.CharField(max_length=100)
    def __str__(self):
        return self.text

class Comment(models.Model):
    state = models.ForeignKey(State)
    side = models.ForeignKey(Side)
    text = models.CharField(max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True)
    by = models.CharField(max_length=100)
    def __str__(self):
        return self.text