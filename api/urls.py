from django.urls import path
from . import views
urlpatterns = [
    path('taches/', views.TacheListCreate.as_view()),
    path('taches/<int:pk>', views.TacheRetrieveUpdateDestroy.as_view()),
]