from rest_framework import generics

from blog.models import Consultation
from .serializers import ConsultationSerializer


class ConsultationCreateAPIViews(generics.CreateAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer


