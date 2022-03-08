from rest_framework import serializers
from .models import Horror_genre, Action

class Horrormodelserializer(serializers.ModelSerializer):
    class Meta:
        model = Horror_genre
        fields = ['movie_name', 'dirctor_name', 'production_year']

class Actionmodelserializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = '__all__'

