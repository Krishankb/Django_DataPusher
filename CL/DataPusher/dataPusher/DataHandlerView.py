import json
from urllib.parse import urlencode
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import Account, Destination
import requests

class DataHandlerView(APIView):

    def post(self, request):
        data = json.loads(request.body)
        token = request.META.get('HTTP_CL_X_TOKEN')
        if not token:
            return JsonResponse({"error": "Unauthenticated"}, status=401)
        try:
            account = Account.objects.get(app_secret_token=token)
        except Account.DoesNotExist:
            return JsonResponse({"error": "Invalid token"}, status=401)
        destinations = Destination.objects.filter(account=account)
        for destination in destinations:
            url = destination.url
            http_method = destination.http_method
            headers = destination.headers
            if http_method == "GET":
                if not all(key in data for key in ('key1', 'key2')):
                    return JsonResponse({"error": "Invalid Data"}, status=400)
                data = urlencode(data)
                url = f"{url}?{data}"
            else:
                headers["Content-Type"] = "application/json"
            response = requests.request(http_method, url, headers=headers, json=data)
            if response.status_code != 200:
                return JsonResponse({"error": "Failed to send data"}, status=500)
        return JsonResponse({"message": "Data sent successfully"})
