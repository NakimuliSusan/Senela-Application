import random
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from django.contrib.auth.hashers import make_password
from .send_sms import send_sms




@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        sms_sender = send_sms()

        # Generate and send OTP via SMS
        otp = generate_otp()

        if otp:
            # Send the OTP to the user's phone number
            sms_sender.send(user.phoneNumber, otp)

            # Store the hashed OTP in the user details
            user_details = User.objects.get(id=user.id)
            user_details.hashed_otp = make_password(otp)
            user_details.save()
            print(user_details)

            return Response({'message': 'User registered successfully. OTP sent via SMS.'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Failed to send OTP via SMS.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def login_user(request):
    username = request.data.get('userName')
    password = request.data.get('password')

    try:
        user = User.objects.get(userName=username, password=password)
    except User.DoesNotExist:
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

def generate_otp():
    # Generate a 6-digit random OTP
    return str(random.randint(100000, 999999))