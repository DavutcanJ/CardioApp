from rest_framework import generics,status
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer,UserResponseSerializer
from rest_framework.views import APIView
from keras import models
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
import pandas as pd
import numpy as np
class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(operation_description="List all users or create a new user")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new user")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)



class UserListRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field="pk"

    @swagger_auto_schema(operation_description="Retrieve a user by id")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update a user by id")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a user by id")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    
class UserDiseaseRate(APIView):
    lookup_field="pk"
    @swagger_auto_schema(operation_description="Get disease rate for a user by id and update it")
    def get(self,request,format=None,pk=0):
        users = User.objects.filter(id=pk).values()
        a = list(users[0].values()) 
        del a[0]
        del a[0]
        del a[len(a)-1]
        testdata = np.array(a)
        testdata = testdata.reshape(1, 11)
        model = models.load_model("./YetmisDogruluk.keras")
        rate = model.predict(testdata)
        print(rate)
        User.objects.filter(id=pk).update(cardisrate=rate)
        
        serializer = UserResponseSerializer(users,many=True)   
        return Response(serializer.data,status= status.HTTP_200_OK)
    

class UserDiseaseData(APIView):

    @swagger_auto_schema(operation_description="Get disease data for all users")
    def get(self, request, format=None):
        # Read the data from the CSV file
        data = pd.read_csv('cardio_train.csv')

        # Convert the data to a list of dictionaries
        users = data.to_dict('records')

        # Return the data as the response
        return Response(users, status=status.HTTP_200_OK)