import json
from django.views import View
from .models import Users
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class MainView(View):

    def post(self, request):
        data = json.loads(request.body)
        Users(
              name = data['name'],
              email = data['email'],
              password = data['password']
        ).save()
        return JsonResponse({'message':'success'}, status=200)



    def get(self, request):
        user_data = Users.objects.values()
        return JsonResponse({'users':list(user_data)}, status=200)




