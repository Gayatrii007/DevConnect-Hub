from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def health_check(request):
    return Response({"status": "alive", "message": "DevConnect Hub is ready!"})
