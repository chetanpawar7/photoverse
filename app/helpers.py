from app.utils.response_utils import success_response, error_response, translator_response
from app.utils import message_conf
from rest_framework import status
from app.utils import system_errors , instance_utils ,common_utils
from django.contrib.auth.hashers import check_password
from app.models import User
from app.serializers import PostMasterSerializer
from app.utils import storage_utils
import json
import requests
from photoverse_backend import settings


def register_user(self, data):
    try:
        first_name = data.get('first_name','')
        last_name = data.get('last_name','')
        username = data.get('username','')
        password = data.get('password','')
        confirm_password = data.get('confirm_password','')
        profile_pic = data.get('profile_pic',''),
        email = data.get('email','')
        
        if not username and not email and not password and not confirm_password:
            return error_response(data=message_conf.REQUIRED_FIELDS_MISSING, status_code=status.HTTP_400_BAD_REQUEST)
        kwargs = {'username': username, 'password': password,'email': email,}
        if profile_pic:
            kwargs['profile_pic'] = profile_pic
            
        if first_name:

            kwargs['first_name'] = first_name
        
        if last_name:
            kwargs['last_name'] = last_name
            
        User.objects.create_user(**kwargs)
        response_data = translator_response(message=message_conf.USER_REGISTERED_SUCCESSFULLY)
        return success_response(data=response_data, status_code=201)

    except Exception as e:
        return system_errors.helper_exception(e, self.get_view_name())
    
    
def login_user(self, data):
    try:
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return error_response(data=message_conf.REQUIRED_FIELDS_MISSING, status_code=412)
        
        user = instance_utils.get_user_instace(username=username)
        if not user:
            return error_response(data=message_conf.INVALID_CREDENTIALS, status_code=401)
        
        if not check_password(password, user.password):
            return error_response(data=message_conf.INVALID_CREDENTIALS, status_code=401)
        
        host = self.request.get_host()
        scheme = self.request.scheme
        
        token_data = common_utils.get_token(scheme,host,username,password)
        response_data = translator_response(message=message_conf.USER_LOGIN_SUCCESSFULLY,token=token_data)
        return success_response(data= response_data, status_code=200)
    except Exception as ex:
        return system_errors.helper_exception(ex, self.get_view_name())
    

def refresh_token(self, data):
    try:
        refresh_token = data.get('refresh_token')
        
        if not refresh_token:
            return error_response(data=message_conf.REQUIRED_FIELDS_MISSING, status_code=412)
        
        host = self.request.get_host()
        scheme = self.request.scheme
        
        token_data = common_utils.get_token_from_refresh_token(scheme, host,refresh_token)
        if not token_data:
            return error_response(data=message_conf.INVALID_REFRESH_TOKEN, status_code=401)
        
        host = self.request.get_host()
        scheme = self.request.scheme
        
        new_token_data = common_utils.get_token(scheme, host, token_data['username'], token_data['password'])
        response_data = translator_response(message=message_conf.TOKEN_REFRESHED_SUCCESSFULLY, token=new_token_data)
        return success_response(data=response_data, status_code=200)
    except Exception as ex:
        return system_errors.helper_exception(ex, self.get_view_name())
    

def logout_user(self, token):
    try:
        host = self.request.get_host()
        scheme = self.request.scheme
        response_data = translator_response(message=message_conf.USER_LOGOUT_SUCCESSFULLY)
        return success_response(data=response_data, status_code=200)
    except Exception as ex:
        return system_errors.helper_exception(ex, self.get_view_name())
    