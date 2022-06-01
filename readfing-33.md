# JSON web 
source - https://jwt.io/introduction/

JSON Web Token (JWT) is an open standard (RFC 7519) that defines a compact and self-contained way for securely 
transmitting information between parties as a JSON object. This information can be verified and trusted because it 
is digitally signed. JWTs can be signed using a secret (with the HMAC algorithm) or a public/private key pair using 
RSA or ECDSA.

Authorization: This is the most common scenario for using JWT. Once the user is logged in, each subsequent request 
will include the JWT, allowing the user to access routes, services, and resources that are permitted with that token. 
Single Sign On is a feature that widely uses JWT nowadays, because of its small overhead and its ability to be easily 
used across different domains.

Information Exchange: JSON Web Tokens are a good way of securely transmitting information between parties. Because 
JWTs can be signed—for example, using public/private key pairs—you can be sure the senders are who they say they are. 
Additionally, as the signature is calculated using the header and the payload, you can also verify that the content 
hasn't been tampered with.

# JWT Authentication
source
https://simpleisbetterthancomplex.com/tutorial/2018/12/19/how-to-use-jwt-authentication-with-django-rest-framework.html

The JWT is just an authorization token that should be included in all requests:

curl http://127.0.0.1:8000/hello/ -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoi
YWNjZXNzIiwiZXhwIjoxNTQzODI4NDMxLCJqdGkiOiI3ZjU5OTdiNzE1MGQ0NjU3OWRjMmI0OTE2NzA5N2U3YiIsInVzZXJfaWQiOjF9.Ju70kdcaHKn1
Qaz8H42zrOYk0Jx9kIckTn9Xx7vhikY'

header

    {
      "typ": "JWT",
      "alg": "HS256"
    }

payload

    {
      "token_type": "access",
      "exp": 1543828431,
      "jti": "7f5997b7150d46579dc2b49167097e7b",
      "user_id": 1
    }

settings.py

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework_simplejwt.authentication.JWTAuthentication',
        ],
    }

urls.py

    from django.urls import path
    from rest_framework_simplejwt import views as jwt_views
    
    urlpatterns = [
        # Your URLs...
        path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    ]

views.py
    
    from rest_framework.views import APIView
    from rest_framework.response import Response
    from rest_framework.permissions import IsAuthenticated
    
    
    class HelloView(APIView):
        permission_classes = (IsAuthenticated,)
    
        def get(self, request):
            content = {'message': 'Hello, World!'}
            return Response(content)
urls.py
    
    from django.urls import path
    from myapi.core import views
    
    urlpatterns = [
        path('hello/', views.HelloView.as_view(), name='hello'),
    ]

