from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers,status
from drf_spectacular.utils import extend_schema
from .models import CustomUser
from .serializer import UserSerializer,LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken



# Create your views here.

def generate_token_user(user):
    token = RefreshToken.for_user(user)  # Create a token for the user instance
    return {
        'refresh_token': str(token),
        'access_token': str(token.access_token)
    }

@extend_schema(request=UserSerializer)
@api_view(['POST'])
def signUp(request):
    serializer = UserSerializer(data=request.data)
    email = request.data.get('email')
    if CustomUser.objects.filter(email=email).exists():
        return Response( {
            'message':'Email already exists',
            'status':status.HTTP_400_BAD_REQUEST,
        })
    
    if serializer.is_valid():
        last_id = CustomUser.objects.all().order_by('user_id').last()
        if last_id:
            id = int(last_id.user_id[2:])
            new_id = id +1
            user_id = f"VM{new_id:05}"
            user = serializer.save(user_id=user_id)
            user.set_password(request.data.get('password'))
            token = generate_token_user(user)
            return Response({'status':status.HTTP_201_CREATED,
            'message':f'Signup succesfull with id {user_id}',
            'data':token
            })
        else:
            new_id = 1
            user_id = f"VM{new_id:05}"
            user = serializer.save(user_id=user_id)
            user.set_password(request.data.get('password'))
            token = generate_token_user(user)
            return Response({'status':status.HTTP_201_CREATED,
            'message':f'Signup succesfull with id {user_id}',
            'data':token
            })
    

    else:
        return Response({
            'message':'signup failed',
            'status':status.HTTP_400_BAD_REQUEST,
            'errors':serializer.errors
           

        })

@extend_schema(request=LoginSerializer)
@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    data = CustomUser.objects.filter(email=email,password=password).first()

    if data:
        token = generate_token_user(data)
        users_data = UserSerializer(data)
        return Response({
            'message':'login successfull',
            'token':token,
            'data':users_data.data
        })



@api_view(['GET'])
def showAllUsers(request):
    users = CustomUser.objects.all()
    serializer = UserSerializer(users,many=True)
    if not serializer:
        return Response({
            'message':'No users found',
            'status':status.HTTP_200_OK,
           
        })
    else:
            return Response({
            'message':'users fetched successfully',
            'status':status.HTTP_200_OK,
            'data': serializer.data
        })
    
