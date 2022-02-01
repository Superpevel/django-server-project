from os import name
from django.views.generic.list import ListView
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from .models import GreatQ
import json


class QuotesView(ListView):
    model = GreatQ
    template_name  = "quotes.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def index(request):

    return render(request, "index.html")


class BackEnd(APIView):

    def post(self, request):

        return Response(f"hello {request.POST.get('name')}")   

class BackEndQuote(APIView):

    def post(self, request):
        quote = request.POST.get('name')
        saves = GreatQ(name='Георгий',quote=quote,year=2022)
        saves.save()
        return Response(f"hello")   