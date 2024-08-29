from rest_framework.response import Response
from rest_framework import status


def translator_response(success=True, message=None, token=None, count=None, total_count=None, data=None):
    response_dict = {}
    if success:
        response_dict['success'] = success
    if message:
        response_dict['message'] = message
    if count:
        response_dict['count'] = count
    if total_count:
        response_dict['total_count'] = total_count
    if token:
        response_dict['token'] = token
    if data:
        response_dict['data'] = data
    return response_dict

def success_response(data: dict = None, status_code: int = status.HTTP_200_OK):
    return Response(data=data, status=status_code)

def error_response(data: dict = None, status_code: int = status.HTTP_412_PRECONDITION_FAILED):
    return Response(data=data, status=status_code)
