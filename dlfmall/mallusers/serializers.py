from rest_framework import serializers

class useDetailsSerialaizer(serializers.Serializer):
    name=serializers.CharField(max_length=50)
    email=serializers.EmailField()
    mobile=serializers.IntegerField()
    password=serializers.CharField(max_length=50)
    address=serializers.CharField(max_length=50)

   
class EventDetailsSerializer(serializers.Serializer):
    eventName = serializers.CharField(max_length=50)
    eventDiscription = serializers.CharField(max_length=100)
    eventDate = serializers.DateTimeField()
    eventVenue = serializers.CharField(max_length=50)
