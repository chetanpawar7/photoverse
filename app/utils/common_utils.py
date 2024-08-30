import requests
import json
from photoverse_backend import settings

def get_token(scheme,host,username,password):
    try:
        url = f"{scheme}://{host}/{settings.CREATE_TOKEN_ENDPOINT}"
        payload = {
            "username": username,
            "password": password
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        if response.status_code == 200:
            return response.json()
    except Exception as ex:
        return ex

def get_token_from_refresh_token(scheme,host,refresh_token):
    try:
        url = f"{scheme}://{host}/{settings.REFRESH_TOKEN_ENDPOINT}"
        headers = {
        'Content-Type': 'application/json',
        }

        payload = {
            'refresh': refresh_token
        }
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        if response.status_code == 200:
            return response.json()
    except Exception as ex:
        return ex
    
def get_verify_token():
    try:
        url = f"{scheme}://{host}/{settings.VERIFY_TOKEN_ENDPOINT}"
    except Exception as ex:
        return ex
    
def revoke_token(scheme, host, ):
    try:
        url = f"{scheme}://{host}/{settings.REVOKE_TOKEN_ENDPOINT}"
        headers = {
        'Content-Type': 'application/json',
        }

        payload = {
            'refresh': refresh_token
        }
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        if response.status_code == 200:
            return response.json()
    except Exception as ex:
        return ex