from .models import Noun
from rest_framework import serializers

class NounSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noun
        # fields = ('id', 'nom_sing', 'gen_sing', 'gender', 'declension', 'definition', 'chapter')
        fields = ('__all__')