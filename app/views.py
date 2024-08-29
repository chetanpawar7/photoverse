from django.shortcuts import render
from rest_framework.views import APIView
from . import helpers
from app.utils import system_errors


class RegisterUserView(APIView):
    def post(self, request):
        try:
            data = request.data
            return helpers.register_user(self, data)
        except Exception as e:
            return system_errors.class_exception(e, self.get_view_name())


class MakePostView(APIView):
    def post(self, request):
        try:
            data = request.data
            user = request.user.id
            return helpers.make_post(self, data, user)
        except Exception as e:
            return system_errors.class_exception(e, self.get_view_name())
