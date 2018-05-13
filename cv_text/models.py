from django.db import models

class Text(models.Model):
    text = models.TextField()

    def post(self):
            self.save()

    def __str__(self):
        return self.text

class VJText(models.Model):
    vjtext= models.TextField()

    def publish(self):
        self.save()
