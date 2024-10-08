from django.db import models

# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=255)
    sound = models.CharField(max_length=255)

    def speak(self) -> str:
        return f'The {self.name} says "{self.sound}"'
