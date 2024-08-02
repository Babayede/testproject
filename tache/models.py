from django.db import models
from django.contrib.auth.models import User

class Tache(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    datecheance = models.DateField()
    status = models.BooleanField(default=False)
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre