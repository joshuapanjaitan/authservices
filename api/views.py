from django.shortcuts import render
from django.http import JsonResponse, response
from django.db.models import Q
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import  IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import Group,User
from django.contrib.auth import authenticate,login,logout

from api import serializers

# Create your views here.
# Create your views here.
@api_view(['GET'])
def api_overview(request):
    api_url = {
        'Auth Login':'/auth-list/',
        'Auth Register':'/auth-register/',

    }
    return Response(api_url)

@api_view(['GET'])
def userList(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)




@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def authentication(request):
    fetch  = request.data
    try:
        uname = fetch["username"]
        pwd = fetch["password"]
        user = authenticate(request,username=uname, password = pwd)
        group = user.groups.all()[0].name
        if user is not None and group == 'management':
            stat =  User.objects.filter(username = user).values()[0]['is_active'] #get Status activation
            
            response = JsonResponse(data= {
                'message':"Access Successfuly",
                'status_code':200,
                'auth_value':stat,
            })
            response.status_code = 200
        elif group != 'management':
            response = JsonResponse(data= {
                'message':"Not Authorized",
                'status_code':401,
                'auth_value':False,
            })
            response.status_code = 401
        
    except:
        response = JsonResponse(data= {
            'message':"Something went Wrong, Check your Username or Password",
            'status_code':406,
            'auth_value':False,
        })
        response.status_code = 406

    return response
