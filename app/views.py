from django.shortcuts import render
from rest_framework.views import APIView
from . import helpers
from app.utils import system_errors
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
class RegisterUserView(APIView):
    def post(self, request):
        try:
            data = request.data
            return helpers.register_user(self, data)
        except Exception as e:
            return system_errors.class_exception(e, self.get_view_name())

class LoginUserView(APIView):
    def post(self, request):
        try:
            data = request.data
            return helpers.login_user(self, data)
        except Exception as e:
            return system_errors.class_exception(e, self.get_view_name())
        

class RefreshTokenView(APIView):
    def post(self, request):
        try:
            data = request.data
            return helpers.refresh_token(self, data)
        except Exception as e:
            return system_errors.class_exception(e, self.get_view_name())
        

class LogoutApiView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            token = request.auth
            return helpers.logout_user(self,token)
        except Exception as e:
            return system_errors.class_exception(e, self.get_view_name())

class MakePostView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            data = request.data
            user = request.user
            return helpers.make_post(self, data, user)
        except Exception as e:
            return system_errors.class_exception(e, self.get_view_name())
