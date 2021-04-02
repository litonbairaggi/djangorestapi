from rest_framework import serializers 
from main_app.models import Tutorial


class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Tutorial
        fields = ('__all__')