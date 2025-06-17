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
    