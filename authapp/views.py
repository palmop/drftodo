from rest_framework.generics import GenericAPIView
from rest_framework import response, status, permissions
from django.contrib.auth import authenticate
from authapp.serializers import RegisterUserAppSerializer, LoginSerializer


class RegisterUserApp(GenericAPIView):

    # with this property we override settings.REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES']
    # so this viewset is open with empty list []
    authentication_classes = []
    
    serializer_class = RegisterUserAppSerializer

    def get(self, request):
        pass

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():  #check data
            serializer.save()      #implement create method
            return response.Response(serializer.data, status.HTTP_201_CREATED) 
            # note that password is write_only in serializer so
            # does not sent back to the client.
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


    def put(self, request):
        pass

    def delete(self, request):
        pass


class LoginUserApp(GenericAPIView):
     
    # with this property we override settings.REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES']
    # so this viewset is open with empty list []
    authentication_classes = []

    serializer_class = LoginSerializer

    def post(self, request):
        
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        
        user = authenticate(username=email, password=password)
        
        if user:
            serializer=self.serializer_class(user)
            return response.Response(serializer.data, status.HTTP_200_OK)    

        return response.Response({'status': 'KO', 'message': 'bad credentials'}, status.HTTP_401_UNAUTHORIZED)


class UserInfo(GenericAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = LoginSerializer

    def get(self, request):
        user = request.user
        serializer = LoginSerializer(user)
        return response.Response({'user':serializer.data}, status.HTTP_200_OK)

    