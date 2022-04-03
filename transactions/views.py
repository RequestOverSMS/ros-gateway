from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from google.protobuf.json_format import MessageToJson
from transactions.v1_payments_request_pb2 import v1_payments_request
from transactions.ROSRequest_pb2 import ROSRequest
from transactions.ROSEnums_pb2 import Method
from transactions.HTTPHeaders_pb2 import Headers
import json
import base64
import zlib

# Create your views here.


class ROSView(APIView):
    def get(self, request):
        try:
            message = request.query_params.get('Body', "")

            # Decode
            body_compressed = base64.b64decode(message)

            # Decompress
            body = zlib.decompress(body_compressed)

            # Parse protobuf
            ros_received = ROSRequest()
            ros_received.ParseFromString(body)
            ros_message_received = MessageToJson(ros_received)

            if ros_received.uri == "https://api.mercadopago.com/v1/payments" and ros_received.method == Method.GET:
                headers = Headers()
                headers.ParseFromString(ros_received.headers)
                headers_received = MessageToJson(headers)

                body = v1_payments_request()
                body.ParseFromString(ros_received.body)
                body_received = MessageToJson(body)

                print("HEADERS:")
                print(headers_received)
                print()
                print("BODY:")
                print(body_received)
            return Response(data="ROS successful request", status=200)
        except Exception as e:
            print(e)
            return HttpResponse('ROS Bad request', status=400)

