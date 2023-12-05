from django.db import models

# Create your models here.
class PulsChoice(models.Model):
    value = models.CharField(max_length=255)
    def __str__(self):
        return self.value

    

class puls(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    fchoice = models.ForeignKey(PulsChoice, related_name='fch', on_delete=models.PROTECT, null=True, blank=True)
    schoice = models.ForeignKey(PulsChoice, related_name='sch', on_delete=models.PROTECT, null=True, blank=True)

    firstVote = models.IntegerField(default=0)
    secondVote = models.IntegerField(default=0)

    winVote = models.IntegerField(default=50)
    def __str__(self):
        return self.title

 



