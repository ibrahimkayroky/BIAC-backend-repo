
import requests
from rest_framework.views import APIView
from rest_framework.response import Response 
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated

 
from .serializers import imageSerializer
from rest_framework.parsers import (MultiPartParser, FormParser)
from rest_framework import status






# class UploadImageView(APIView):
#     serializer_class = imageSerializer
#     parser_classes = [MultiPartParser, FormParser]

#     def post(self, request):
#         serializer = imageSerializer(data=request.data,context={'request': request})
#         if serializer.is_valid():
#             image = serializer.save()
#             image_id = image.id 
#             response = requests.post(f'http://192.168.1.10:8080/classification/classified_image/{image_id}/')
#             return Response(response.json(), status=response.status_code)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UploadImageView(APIView):
    serializer_class = imageSerializer
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        serializer = imageSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            image = serializer.save()
            image_id = image.id
            response = requests.post(f'http://192.168.1.2:8080/classification/classified_image/{image_id}/')
            response_data = response.json()
            
            image_url = response_data["processed_image_data"]["image_with_model_classification"]
            absolute_image_url = request.build_absolute_uri(image_url)
            
            response_data["processed_image_data"]["image_with_model_classification"] = absolute_image_url
            
            return Response(response_data, status=response.status_code)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



        

