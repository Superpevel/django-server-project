from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions
import json



def index(request):
    return render(request, "index.html")


class BackEnd(APIView):

    def post(self, request):

        return Response(f"hello {request.POST.get('name')}")   