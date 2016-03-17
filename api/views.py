from rest_framework import permissions
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

token = '6d82549b48a8b079f618ee9c51a6dfb59c7e2196'


class TaskList(APIView):
    parser_classes = (JSONParser,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request, format=None):
        return Response({'received data': request.data})
