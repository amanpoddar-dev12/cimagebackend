from rest_framework.views import APIView
from django.http import JsonResponse
from .serializers import *
from .models import *

class userSignup(APIView):
    def post(self,request):
       serializersData=useDetailsSerialaizer(data=request.data)
       if serializersData.is_valid():
           userDetails.objects.create(**serializersData.data)
           message={"message":"User created Successfully"}
           return JsonResponse(message)
       return JsonResponse(serializersData.errors)
    
class userMembership(APIView):
    def get(self,request,email):
        result=list(membershipDetails.objects.filter(email=email).values())
        message={"Membership Details":result}
        return JsonResponse(message,safe=False)
    

class createEvent(APIView):
    def post(self, request):
        serializer = EventDetailsSerializer(data=request.data)
        if serializer.is_valid():
            eventDetails.objects.create(**serializer.validated_data)
            return JsonResponse({"message": "Event created successfully"})
        return JsonResponse(serializer.errors, status=400)

class getEventDetails(APIView):
    def get(self,request):
        result=list(eventDetails.objects.values())
        message={"Event Details":result}
        return JsonResponse(message,safe=False)
