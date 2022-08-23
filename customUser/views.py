from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import CustomUserModel
from .serializers import CustomUserSerializer


@api_view(['GET', 'POST'])
def CustomUserView(request):

    if request.method == 'GET':
        users = CustomUserModel.objects.all()  # fetch all the items

        serializer = CustomUserSerializer(users, many=True)

        return JsonResponse({"users": serializer.data}, )  # if not return an object like in this case add ,safe=False after serializer.data

    if request.method == 'POST':

        serializer = CustomUserSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
