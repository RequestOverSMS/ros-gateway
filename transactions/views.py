from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class ROSView(APIView):
    def get(self, request):
        try:
            print(request.query_params)
            return Response(data="ROS successful request", status=200)
        except Exception as e:
            print(e)
            return HttpResponse('ROS Bad request', status=400)

