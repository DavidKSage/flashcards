from .serializers import NounSerializer
from rest_framework import viewsets
from .models import Noun

# Create your views here.
class NounViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = NounSerializer
    queryset = Noun.objects.all()