# exceptions.py

from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler
from rest_framework.response import Response

from rest_framework.exceptions import APIException
from rest_framework import status


class InvalidAuthorID(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'O ID do autor fornecido não corresponde a nenhum autor existente.'
    default_code = 'invalid_author_id'
