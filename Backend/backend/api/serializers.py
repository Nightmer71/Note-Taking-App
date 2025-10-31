from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}} # Write only makes it so no one can read the password, just write one
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data) #** splits up the keyword arguments
        return user
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {
            "author" : {"read_only" : True}, # Read only makes it so the author can only be read
            "created_at": {"format": None},
        } 