from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from google.protobuf.json_format import MessageToJson
from google.protobuf.json_format import Parse, ParseDict
from transactions.v1_payments_request_pb2 import v1_payments_request
from transactions.v1_btcmarket_response_pb2 import v1_btcmarket_response
from transactions.ROSRequest_pb2 import ROSRequest
from transactions.ROSEnums_pb2 import Method
from transactions.HTTPHeaders_pb2 import Headers
import json
import base64
import zlib
import requests
from twilio.rest import Client
from django.conf import settings

# Create your views here.


class ROSView(APIView):
    def get(self, request):
        try:
            from_number = request.query_params.get('From', "")

            print('Starting processing pipeline...')
            message = request.query_params.get('Body', "")
            message = message.replace(' ', '+')

            # Decode
            print('Starting decoding with ', message)
            body_compressed = base64.b64decode(message)

            # Decompress
            print('Starting decompressing with ', body_compressed)
            body = zlib.decompress(body_compressed)

            # Parse protobuf
            print('Starting protobuf decoding with ', body)
            ros_received = ROSRequest()
            ros_received.ParseFromString(body)
            ros_message_received = MessageToJson(ros_received)


            headers = ros_message_received['headers']
            body = ros_message_received['body']
            method = ros_message_received['method']
            uri = ros_message_received['uri']

            if uri == "https://api.mercadopago.com/v1/payments" and method == Method.GET:
                response = requests.request(method, uri, headers=headers, data=body)
                print('Received response')
                print(response.content)

            #
            #
            # if ros_received.uri == "https://api.mercadopago.com/v1/payments" and ros_received.method == Method.GET:
            #     headers = Headers()
            #     headers.ParseFromString(ros_received.headers)
            #     headers_received = MessageToJson(headers)
            #
            #     body = v1_payments_request()
            #     body.ParseFromString(ros_received.body)
            #     body_received = MessageToJson(body)
            #
            #     print("HEADERS:")
            #     print(headers_received)
            #     print()
            #     print("BODY:")
            #     print(body_received)

            if uri == 'https://api.coindesk.com/v1/bpi/currentprice.json' and method == Method.GET:
                response = requests.request(method, uri, headers=headers, data=body)
                print('Received response')
                print(response.content)

                body = ParseDict(response.content, v1_btcmarket_response()).SerializeToString()

                ros = ROSRequest()
                ros.method = ros_received.method
                ros.uri = ros_received.uri
                # ros.headers = headers
                ros.body = body

                ros_str = ros.SerializeToString()
                print('Processing protobuf', ros_str)
                body_compressed = zlib.compress(ros_str, level=9)
                print('Processing compress', body_compressed)
                body_encoded = base64.b64encode(body_compressed)
                print('Processing encoded', body_encoded)

                account_sid = settings.TWILIO_ACCOUNT_ID
                auth_token = settings.TWILIO_AUTH_TOKEN
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                    body=f'{body_encoded}',
                    from_='+16064044957',
                    to=from_number
                )
            return Response(data="ROS successful request", status=200)
        except Exception as e:
            print(e)
            return HttpResponse('ROS Bad request', status=400)

