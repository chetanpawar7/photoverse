from rest_framework.response import Response
from app.utils import message_conf
from app.utils import response_utils


def class_exception(exception, class_name):
    return Response(
        data=message_conf.API_FAILURE,
        status=500
    )


def helper_exception(exception, view_name):
    return Response(
        data=message_conf.SOMETHING_WENT_WRONG,
        status=412
    )
