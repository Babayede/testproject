from rest_framework import generics, permissions
from .serializers import TacheSerializer
from tache.models import Tache

class TacheListCreate(generics.ListCreateAPIView):
    serializer_class = TacheSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Tache.objects.filter(user=user).order_by('-datecheance')
    def perform_create(self, serializer):
        #serializer prends en main le model django 
        serializer.save(user=self.request.user)
class TacheRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TacheSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
    # user peut uniquement update, delete 
        return Tache.objects.filter(user=user)