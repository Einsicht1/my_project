from django.shortcuts import render
from django.http import HttpResponse


def hi(request):
    return HttpResponse('돈까스 모임')



# Create your views here.
