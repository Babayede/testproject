from rest_framework import serializers
from tache.models import Tache

class TacheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tache
        fields = ['id','titre','description','datecheance','status', 'attachment']