from django.db import models

class StampType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Stamp(models.Model):
    type = models.ForeignKey(StampType, on_delete=models.CASCADE)
    time = models.DateTimeField('Time for stamp')

    def __str__(self):
        return "{}, {}".format(self.type, self.time)
