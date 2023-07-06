import random
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer



@api_view(['POST']) 
def user_registration(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer_data = serializer.data
        user = serializer.save()
        print( Response({
            "user_info": serializer_data,
            "user": user,
            "Message": "Successfully registered"
        }, status=201))
        return Response({
            "user_info": serializer_data,
            "user": user,
            "Message": "Successfully registered"
        }, status=201)
      
    return Response(serializer.errors, status=400)
    
# def user_registration(request):
#     if request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             # Extract the required parameters from the request data
#             firstname = request.data.get('firstName')
#             lastname = request.data.get('lastName')
#             phone_number = request.data.get('phoneNumber')
#             email = request.data.get('email')


#             # Generate a unique user ID
#             user_id = generate_user_id()

#             # Send the OTP to the user's email
#             otp = generate_otp()
#             send_otp_email(email, otp)

#             # Save the user ID and OTP to the user model or database
#             user = User(firstname=firstname, lastname= lastname, phone_number=phone_number, email=email, user_id=user_id, otp=otp)
#             user.save()

#             serializer = UserSerializer(user)

#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
    

@api_view(['GET'])
def get_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)  # Use the serializer for User model
        return Response(serializer.data)
    else:
        return Response(status=400)

@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('userName')
        otp = request.data.get('otp')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'error': 'Invalid username'}, status=400)

        if not user.otp_verified:
            return Response({'error': 'OTP verification required'}, status=400)

        if otp != user.otp:
            return Response({'error': 'Invalid OTP'}, status=400)

        # Generate a random password for the user
        password = generate_random_password()
        # user.set_password(password)
        user.save()

        # Authenticate the user with the generated password
        authenticated_user = authenticate(request, username=username, password=password)
        if not authenticated_user:
            return Response({'error': 'Invalid username or password'}, status=400)

        # Create a session for the authenticated user
        login(request, authenticated_user)

        return Response({'message': 'User login successful'}, status=200)

def generate_otp():
    digits = "0123456789"
    otp = ""
    for _ in range(6):
        otp += random.choice(digits)
    return otp

def send_otp_email(email, otp):
    subject = 'Your OTP'
    message = f'Your OTP is: {otp}'
    from_email = 'your_email@example.com'
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)

def generate_user_id():
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    password = ''.join(random.choice(chars) for _ in range(10))
    return password

def generate_random_password():
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    password = ''.join(random.choice(chars) for _ in range(10))
    return password

