from hashlib import algorithms_available
from rest_framework.authentication import get_authorization_header, BaseAuthentication
from rest_framework import exceptions
import jwt
from django.conf import settings
from authapp.models import UserApp

# rif. https://www.django-rest-framework.org/api-guide/authentication/#custom-authentication
# to set in settings this class under REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES']
class JWTAuth(BaseAuthentication):

    # implement authenticate method
    def authenticate(self, request):

        auth_header = get_authorization_header(request)
        auth_data = auth_header.decode("UTF-8")
        # we split "Bearer ey...."
        auth_token = auth_data.split(" ")
        if len(auth_token) != 2:
            raise exceptions.AuthenticationFailed('invalid token')
        token = auth_token[1]
        print("token : {}".format(token))
        try: 

            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=("HS256",))
            #print("payload: {}".format(payload))
            email = payload['email']
            #print("email: {}".format(email))
            user = UserApp.objects.get(email=email)
            #print("user: {}".format(user))
            return (user, token)

        except jwt.ExpiredSignatureError as e:
            raise exceptions.AuthenticationFailed('expired token')
        except jwt.DecodeError as e:
            raise exceptions.AuthenticationFailed('invalid token (decode error)')
        except UserApp.DoesNotExist as e:
            raise exceptions.AuthenticationFailed('user does not exists')
