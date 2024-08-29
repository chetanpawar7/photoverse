from app.utils.response_utils import success_response, error_response, translator_response
from app.utils import message_conf
from rest_framework import status
from app.utils import system_errors
from app.models import User
from app.serializers import PostMasterSerializer ,CreateUserSerailizer
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
        
        if not username and not password:
            return error_response(data=message_conf.REQUIRED_FIELDS_MISSING, status_code=status.HTTP_400_BAD_REQUEST)
        
        base_url = settings.BASE_URL
        create_user_endpoint = settings.CREATE_USER
        url = f"{base_url}{create_user_endpoint}"
        if not User.objects.filter(username=username).exists():
            payload = {'username': username,'password': password,'email': email, 're_password': confirm_password}
            data = requests.post(url=url, data=json.dumps(payload))
            if data.status_code == 201:
                data = translator_response(message= message_conf.USER_REGISTERED_SUCCESSFULLY)
                return success_response(data=data,status_code=201)
        
    except Exception as e:
        return system_errors.helper_exception(e, self.get_view_name())
        
        
        
        