import json
from django.views import View
from .models import Users
from django.http import JsonResponse, HttpResponse

class SignUp(View):

    def post(self, request):
        account_data = json.loads(request.body)
        try:
            if not Users.objects.filter(email=account_data['email']).exists():
                Users(
                  name = account_data['name'],
                  email = account_data['email'],
                  password = account_data['password']).save()
                return JsonResponse({'message':'welcome!'}, status=200)
            else:
                return HttpResponse(status=409)
        except KeyError:
            return HttpResponse(status=400)

class SignIn(View):

    def post(self, request):
        account_data = json.loads(request.body)
        try:
            if Users.objects.filter(email=account_data['email']).exists():
                if Users.objects.filter(password=account_data['password']).exists():
                    return JsonResponse({'message':'welcome to westagram!'},status=200)
                else: 
                    return HttpResponse(status=401)
            else:
                return HttpResponse(status=400)
   
        except KeyError:
             return HttpResponse(status=400)
             
