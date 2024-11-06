from django.db import models

# Create your models here.
class Monster(models.Model):
    name = models.CharField(max_length=255)
    monster_type = models.CharField(max_length=100)
    description = models.TextField()
    habitat = models.CharField(max_length=255)
    danger_level = models.IntegerField()  # 1 to 5, where 5 is the most dangerous

    def __str__(self):
        return self.name

