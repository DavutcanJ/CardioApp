from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer,UserResponseSerializer
from rest_framework.views import APIView
import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.models import Sequential, Model, load_model
import os

import numpy as np

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class UserListRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field="pk"
    
class UserDiseaseRate(APIView):
    lookup_field="pk"
    def get(self,request,format=None,pk=0):
        
        users = User.objects.filter(id=pk).values()
        a = list(users[0].values()) 
        del a[0]
        del a[0]
        del a[len(a)-1]
        testdata = np.array(a)
        testdata = testdata.reshape(1, 11)
        model = load_model("../ai/Ellidogruluk.keras")
        rate = model.predict(testdata)
        
        ## Buraya veri degistirilip geri gonderilecek hocaya sor bi
        
        serializer = UserResponseSerializer(users,many=True)   
        return Response(serializer.data,status= status.HTTP_200_OK)
    